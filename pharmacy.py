# Working with JSON Data from GitHub

# importing data
import requests

# defining a variable url(URL pointing to JSON file hosted in GITHUB) and assigns it a string value
url = "https://raw.githubusercontent.com/TeddyRutto/Pharmacy_dataset/refs/heads/main/MOCK_DATA%20(2).json"

# Fetch data from url using requests
pharmacy = requests.get(url)
pharmacy_data = pharmacy.json()

# Display the first 2 items of the fetched data
print(pharmacy_data[:2])

# Check the type of pharmacy_data
print(type(pharmacy_data))

# Convert list to dictionary with prescription_number as key
pharmacy_dict = {item["prescription_number"]: item for item in pharmacy_data}

# Convert the extracted JSON data into a well-structured DataFrame
import pandas as pd

pharmacy_df = pd.DataFrame.from_dict(pharmacy_dict, orient="index")

print(pharmacy_df.head())

# Export to CSV
pharmacy_csv = pharmacy_df.to_csv("pharmacy_csv", index=False)

# ============================================
# Working with DummyJSON API Endpoints
# ============================================

# 1. Define the endpoints
products_url = "https://dummyjson.com/products"
carts_url = "https://dummyjson.com/carts"

# 2. Fetch data from the endpoints
products_set = requests.get(products_url)
carts_set = requests.get(carts_url)

# 3. Convert to JSON
products_data = products_set.json()
carts_data = carts_set.json()

print(f"Total Products found: {len(products_data['products'])}")
print(f"Total Carts found: {len(carts_data['carts'])}")

# 4. Create DataFrames
df_products = pd.DataFrame(products_data['products'])
df_carts = pd.DataFrame(carts_data['carts'])

# 5. Export to CSV
df_products.to_csv('products_dataset.csv', index=False)
df_carts.to_csv('carts_dataset.csv', index=False)
