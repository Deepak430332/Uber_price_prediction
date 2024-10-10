# Uber Price Prediction Full Stack Application

## Project Description

This project is designed to develop a predictive model for estimating Uber fare prices accurately. As the largest ride-hailing service globally, Uber generates vast datasets through its daily transactions. By leveraging this data effectively, the goal is to inform better business decisions and optimize customer satisfaction. A key focus of the project is to predict fare prices with high precision, allowing Uber to improve service efficiency.

This application includes both a machine learning model for fare prediction and a full-stack web interface where users can book trips by providing details like passenger count, trip distance, vehicle type, and more. The app also supports **CRUD (Create, Read, Update, Delete)** operations for trip data and features automated testing for functionality.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Contributions](#contributions)
- [Acknowledgments](#acknowledgments)

---

## Introduction

The project encompasses **Exploratory Data Analysis (EDA)**, **Feature Engineering**, and **Predictive Modeling**. By applying various regression models, we identified the one that yields the highest accuracy in predicting Uber fare prices.

The web interface allows customers to book trips by entering information such as the number of passengers, trip distance, pickup/drop locations, and vehicle type. The application connects to a backend that stores trip details in a database and uses a machine learning model (saved in a pickle file) to predict the fare based on the trip parameters.

CRUD operations are integrated into the app, allowing users to manage trip records. We also implemented **unit testing** to ensure the functionality of all CRUD features. Additionally, a **CI/CD pipeline** has been set up for version control and streamlined code deployment.

---

## Features

The application includes the following key features:

- **Pickup and Drop Time**
- **Trip Distance**
- **Trip Duration**
- **Predicted Fare**
- **Passenger Count**
- **Vehicle Type**
  
---

## Installation

To run the project, follow these steps:

1. Download the project folder as a ZIP file or clone it from the repository.
2. Install the necessary dependencies:

   ```bash
   pip install streamlit
   pip install flask
   pip install joblib
   npm install axios
   ```

3. Ensure the machine learning model (`model.pkl`) is included in the appropriate directory for fare prediction.

---

## Tech Stack

### Frontend

- **React.js**
- **Node.js**

### Backend

- **Flask**
- **Express.js**

### Database

- **MongoDB (NoSQL)**

### Testing & CI/CD

- **Unit Testing** (for CRUD operations)
- **Git** (for version control)
- **CI/CD pipeline** (for continuous integration and deployment)

---

## Contributions

- **Deepak**: EDA, PPT creation, Testing
- **Umesh**: Data preprocessing, Frontend & Backend development
- **Harsha**: Model integration, Data processing, Full-stack development
- **Varshith**: Machine Learning modeling, Data preprocessing, Backend development
- **Bhanu**: Data cleaning, UI enhancement, PPT creation

---

## Acknowledgments

We extend our gratitude to our instructor, **Preety Singh**, for her guidance and mentorship throughout the project. We also appreciate the contributions of all team members who helped bring this project to life.

---

This version provides more clarity and readability while maintaining all the critical project information. Let me know if you need further modifications!
