import streamlit as st
import pandas as pd

## Add a title 
st.title("Flipkart Sales Data")
st.subheader('Raw data obtained from the company')

## Read the CSV file 
df = pd.read_csv('flipkart_sales.csv')
df

from PIL import Image
logo = Image.open('flipkart_logo.png')
st.sidebar.image(logo, width = 300)

# Add a search box 
st.write('Filter by product name')
st.sidebar.subheader('Search Product')
search_product=st.sidebar.text_input("Enter Produce Name")
df[df['ProductName'].str.contains(search_product, case=False)]

# Filtering the data 
st.sidebar.title('Filter Data')

# Filter by City 
st.write("Filter by city")
st.sidebar.subheader('Filter by City')
selected_city = st.sidebar.selectbox('Select City', df['City'].unique())
df[df['City'] == selected_city]

# Filter by Region
st.write("Filter by region")
st.sidebar.subheader('Filter by Region')
selected_region = st.sidebar.selectbox('Select Region', df['Region'].unique())
df[df['Region'] == selected_region]

st.write("Data filteration (no. of orders, total sale, average sale, and total profit) in each city")
# Enter the city name manually
city_name = st.text_input('Enter the City name')

# Number of orders placed 
orders_placed = df[df['City'] == city_name]['OrderID'].count()
st.write('The no. of orders placed ', orders_placed)

# Total sales 
total_sales= df[df['City'] == city_name]['Sales'].sum()
st.write(f'Total sale in {city_name} is {total_sales}')

# Average sale  
average_sales = df[df['City'] == city_name]['Sales'].mean()
st.write(f'Average sale in {city_name} is {total_sales}')

# Total profit 
total_profit = df[df['City'] == city_name]['Profit'].sum()
st.write(f'Total Profit in {city_name} is {total_profit}')


# Create a Pie chart for Region
st.header('Graphical representation')
import matplotlib.pyplot as plt
st.write('Pie Chart for Region')
region_data = df['Region'].value_counts()
st.write(region_data)

fig, ax = plt.subplots()
ax.pie(region_data, labels=region_data.index, autopct='%1.1f%%')
st.pyplot(fig)

# Create a Pie chart for City 
st.write('Pie Chart for City')
city_data=df['City'].value_counts()
st.write(city_data)

fig, ax = plt.subplots()
ax.pie(city_data, labels=city_data.index, autopct='%1.1f%%')
st.pyplot(fig)

# Create a Pie chart for SubCategory
st.write('Pie Chart for SubCategory')
SubCategory_data=df['SubCategory'].value_counts()
st.write(SubCategory_data)

fig, ax = plt.subplots()
ax.pie(SubCategory_data, labels=SubCategory_data.index, autopct='%1.1f%%')
st.pyplot(fig)

# Line chart for sales and profit 
st.write('Line Chart for Sales and Profit')
line_data=df.groupby('OrderDate')[['Sales', 'Profit']].sum()
st.write(line_data)

fig, ax = plt.subplots()
ax.plot(line_data.index, line_data['Sales'],label='Sales')
ax.plot(line_data.index, line_data['Profit'], label='Profit')
ax.legend()
st.pyplot(fig)

