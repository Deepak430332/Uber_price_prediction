import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load your data
# Assuming df is your DataFrame
df = pd.read_csv('uber_data.csv')

# Streamlit app
st.title("Uber Trips Dashboard")
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

# Filters
start_date = st.date_input("Start Date", value=pd.to_datetime(df['tpep_pickup_datetime'].min()))
end_date = st.date_input("End Date", value=pd.to_datetime(df['tpep_pickup_datetime'].max()))
payment_type = st.multiselect("Select Payment Type", options=df['payment_type'].unique())

# Filter data based on inputs
filtered_df = df[(df['tpep_pickup_datetime'] >= pd.to_datetime(start_date)) & (df['tpep_pickup_datetime'] <= pd.to_datetime(end_date))]
if payment_type:
    filtered_df = filtered_df[filtered_df['payment_type'].isin(payment_type)]

# Overview Metrics
total_trips = len(filtered_df)
total_distance = filtered_df['trip_distance'].sum()
total_revenue = filtered_df['total_amount'].sum()
average_fare = filtered_df['fare_amount'].mean()

st.metric("Total Trips", total_trips)
st.metric("Total Distance", f"{total_distance:.2f} miles")
st.metric("Total Revenue", f"${total_revenue:.2f}")
st.metric("Average Fare", f"${average_fare:.2f}")

# Time Series Analysis
filtered_df.set_index('tpep_pickup_datetime', inplace=True)

# Resample and plot
trips_over_time = px.line(filtered_df.resample('D').size().reset_index(name='Trips'), x='tpep_pickup_datetime', y='Trips', labels={'tpep_pickup_datetime': 'Date', 'Trips': 'Number of Trips'})
revenue_over_time = px.line(filtered_df.resample('D')['total_amount'].sum().reset_index(name='Revenue'), x='tpep_pickup_datetime', y='Revenue', labels={'tpep_pickup_datetime': 'Date', 'Revenue': 'Total Revenue'})

st.plotly_chart(trips_over_time)
st.plotly_chart(revenue_over_time)

# Reset the index if needed for further operations
filtered_df.reset_index(inplace=True)

# Geospatial Analysis
st.subheader("Pickup Locations")
pickup_map = px.scatter_mapbox(filtered_df, lat='pickup_latitude', lon='pickup_longitude', zoom=10, height=500)
pickup_map.update_layout(mapbox_style="open-street-map")
st.plotly_chart(pickup_map)

st.subheader("Dropoff Locations")
dropoff_map = px.scatter_mapbox(filtered_df, lat='dropoff_latitude', lon='dropoff_longitude', zoom=10, height=500)
dropoff_map.update_layout(mapbox_style="open-street-map")
st.plotly_chart(dropoff_map)

# Trip Details
trip_distance_distribution = px.histogram(filtered_df, x='trip_distance', nbins=50)
passenger_count_distribution = px.histogram(filtered_df, x='passenger_count', nbins=6)
payment_type_distribution = px.histogram(filtered_df, x='payment_type')

st.plotly_chart(trip_distance_distribution)
st.plotly_chart(passenger_count_distribution)
st.plotly_chart(payment_type_distribution)