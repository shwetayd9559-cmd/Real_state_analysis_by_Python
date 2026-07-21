 🏡 Gurgaon Real Estate Data Analysis

 
 📌 Project Overview
-- This project analyzes a Gurgaon real estate dataset using Python. It includes data cleaning, exploratory data analysis (EDA), and data visualization to identify pricing trends, locality insights, and property characteristics.

🎯 Objectives
- Clean and preprocess the dataset
- Analyze property prices across different localities
- Compare Ready-to-Move vs Under-Construction properties
- Compare RERA-approved and Non-RERA properties
- Identify the most expensive BHK configurations
- Analyze builder-wise pricing
- Study the relationship between area and property price

 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

 📂 Dataset

The dataset used in this project contains real estate property listings from Gurgaon, India. It includes details about residential properties such as price, area, locality, builder, property type, and other important features.

 Dataset Features

- Price
- Area (Square Feet)
- Rate per Sq. Ft.
- Locality
- Property Type
- BHK Count
- Property Status (Ready to Move / Under Construction)
- RERA Approval
- Builder/Company Name

 Data Preprocessing

The following preprocessing steps were performed before analysis:

- Removed duplicate records
- Removed missing values
- Standardized column names
- Converted price and rate per sq. ft. columns to numeric format
- Cleaned categorical values for consistency

 Purpose

The dataset is used to perform Exploratory Data Analysis (EDA) and identify pricing patterns, locality trends, and factors that influence real estate prices in Gurgaon.

 📊 Analysis Performed
✔ Data Cleaning

- Removed duplicate records
- Removed missing values
- Converted price columns into numeric format
- Standardized column names

✔ Exploratory Data Analysis

- Costliest apartment
- Highest average price locality
- Highest rate per square foot
- Ready-to-Move vs Under-Construction comparison
- RERA approval price comparison
- Most expensive BHK configuration
- Property type comparison
- Top builders by price
- Area vs Price visualization
- Area vs Rate per Sq. Ft visualization

 📈 Sample Visualizations( Data Visualizations)

The project includes visualizations to better understand the relationship between property features and pricing.

 1. Impact of Area on Price

This scatter plot shows the relationship between the property area and its selling price.

**Key Insights:**
- Most properties are concentrated in the lower area range.
- Larger properties generally have higher prices.
- A few properties have extremely large areas, creating outliers.
- The presence of outliers suggests that further preprocessing or outlier removal could improve analysis.

-- <img width="1363" height="646" alt="area vs price" src="https://github.com/user-attachments/assets/bf3a67b6-a14c-4d62-acc9-9ae5949913a3" />


### 2. Impact of Area on Rate per Sq. Ft.

This scatter plot illustrates how property area influences the rate per square foot.

**Key Insights:**
- Most properties have a rate between ₹20,000 and ₹100,000 per sq. ft.
- Some properties command exceptionally high rates, indicating premium locations or luxury developments.
- The rate per square foot does not consistently increase with property area, suggesting that location and amenities significantly influence pricing.


-- <img width="1000" height="646" alt="Area vs Rate per Sq  Ft" src="https://github.com/user-attachments/assets/4decfd16-2c1d-49be-9aed-9de2c4132bda" />



