# Sales-DA-Project

This repository contains a Python script that performs sales data analysis by processing and visualizing sales data from multiple CSV files. The goal is to derive insights such as the best month for sales, city with the highest number of orders, and products sold most frequently.

# Features

Combines multiple sales data files into a single DataFrame.
Cleans and preprocesses data by removing null values and ensuring correct data types.

Performs analysis to answer questions such as:
What is the best month for sales?
Which city has the maximum number of orders?
At what time are sales maximized?
What product sold the most and why?
What products are often sold together?
Provides visualizations using Matplotlib to display insights.

# Requirements
To run the script, you need the following dependencies installed:

Python 3.6+
NumPy
Pandas
Matplotlib

# Analysis Performed
Data Merging:
Combines all sales data files into a single DataFrame.
Saves the combined data to all_data.csv for future use.

Data Cleaning:
Removes null values.
Filters out invalid rows (e.g., header rows mixed in the data).
Converts columns to appropriate data types.

Best Month for Sales:
Extracts the month from the Order Date column.
Calculates total sales for each month and visualizes them in a bar chart.

City with Maximum Orders:
Extracts city information from the Purchase Address column.
Groups data by city and visualizes the order count using a bar chart.

Peak Sales Time:
Extracts the hour from the Order Date column.
Plots a line graph to show the number of orders placed at different times of the day.

Top-Selling Products:
Calculates the total quantity ordered for each product.
Visualizes the product sales with a bar chart.
Plots average product prices alongside quantities sold for comparison.

Products Sold Together:
Identifies orders where multiple products were purchased together.
Visualizes the most common product combinations in a pie chart.

# Visualizations
Monthly Sales Bar Chart: Displays total sales for each month.
City-wise Order Count Bar Chart: Highlights which cities had the highest sales.
Sales by Hour Line Graph: Shows peak hours for product sales.
Product Sales Bar Chart: Compares quantities sold for each product.
Common Product Combinations Pie Chart: Highlights frequently sold product combinations.

# Notes
Ensure all sales data files follow a consistent format with columns such as Order Date, Quantity Ordered, Price Each, and Purchase Address.
Adjust file paths (path variable) in the script as per your system's directory structure.
Customize thresholds (e.g., filtering conditions) in the script to suit your data.
