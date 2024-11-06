# streamlitapp.py
import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the Streamlit app
st.title("My First Streamlit App")

# Add a header and subheader
st.header("Welcome to My App")
st.subheader("This is a subheader")

# Add text
st.write("This is a simple Streamlit app example.")

# Add a sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar.")

# User input
name = st.text_input("Enter your name:")
st.write("Hello,", name)

# Adding a slider
age = st.slider("Select your age", 0, 100, 25)
st.write("Your age is:", age)

# Generate and display a random dataframe
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)
st.write("Random DataFrame")
st.dataframe(df)

# Plotting a simple chart
st.write("Simple Line Chart")
st.line_chart(df)

# Conditional display based on a checkbox
if st.checkbox("Show Data Summary"):
    st.write(df.describe())

# File upload
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
