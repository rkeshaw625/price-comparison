import streamlit as st
import pandas as pd
import random

# Simulated data for home delivery apps (as real-time fetching needs APIs or scraping)
def fetch_product_prices(product_name):
    apps = ["Flipkart Minutes", "Swiggy Instamart", "Blinkit", "Big Basket Now", "Zepto"]
    products = []
    
    for app in apps:
        price = round(random.uniform(20, 150), 2)  # Simulated price
        quantity = random.choice(["500g", "1kg", "250g", "2kg"])  # Simulated quantity
        products.append({"App": app, "Product": product_name.capitalize(), "Price (INR)": price, "Quantity": quantity})
    
    return pd.DataFrame(products)

# Streamlit UI
st.title("Grocery Price Comparison App")
st.write("Compare product prices across different home delivery platforms")

# User Input
product_name = st.text_input("Enter product name:", "Tomato")

if st.button("Compare Prices"):
    if product_name.strip():
        result_df = fetch_product_prices(product_name)
        st.write("### Price Comparison")
        st.dataframe(result_df)
    else:
        st.warning("Please enter a valid product name.")
