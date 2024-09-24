import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('uber_data.csv')

# Preprocess the data
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
df.fillna(0, inplace=True)
df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

# Streamlit app
st.title('Uber Data Dashboard')

# Sidebar for user input
st.sidebar.header('Filter Options')
passenger_count = st.sidebar.slider('Passenger Count', 1, 6, 1)
filtered_data = df[df['passenger_count'] == passenger_count]

# Main panel
st.header('Trip Distance Distribution')
fig, ax = plt.subplots()
sns.histplot(filtered_data['trip_distance'], bins=50, kde=True, ax=ax)
st.pyplot(fig)

st.header('Trip Duration Distribution')
fig, ax = plt.subplots()
sns.histplot(filtered_data['trip_duration'], bins=50, kde=True, ax=ax)
st.pyplot(fig)

# Display data
st.header('Filtered Data')
st.write(filtered_data.head())