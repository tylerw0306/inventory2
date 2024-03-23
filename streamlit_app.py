import streamlit as st
import pandas as pd

# Function to load or create the inventory DataFrame
def load_inventory(file_path):
    try:
        inventory_df = pd.read_csv(file_path)
    except FileNotFoundError:
        # If the file does not exist, create an empty DataFrame
        inventory_df = pd.DataFrame(columns=['Item', 'Quantity'])
    return inventory_df

# Save the inventory DataFrame to a CSV file
def save_inventory(inventory_df, file_path):
    inventory_df.to_csv(file_path, index=False)

# Load or create the inventory DataFrame
file_path = "inventory.csv"
inventory_df = load_inventory(file_path)

# Title and section header
st.title('Fridge Inventory')
st.subheader('Add New Item')

# Input fields for adding a new item
new_item_name = st.text_input("Item Name:")
new_item_quantity = st.number_input("Quantity:", min_value=1, step=1)

# Add button to add the new item to the inventory
if st.button("Add Item"):
    if new_item_name and new_item_quantity is not None:
        # Append new item to the inventory DataFrame
        new_item = {'Item': new_item_name, 'Quantity': new_item_quantity}
        inventory_df = inventory_df.append(new_item, ignore_index=True)
        st.success("Item added successfully!")
    elif not new_item_name:
        st.error("Please enter an item name.")
    else:
        st.error("Please enter a quantity.")

# Display the current inventory
st.subheader('Current Inventory')
st.write(inventory_df)

# Save inventory changes when the user exits the app
save_inventory(inventory_df, file_path)
