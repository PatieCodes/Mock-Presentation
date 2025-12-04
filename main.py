import streamlit as st
import pandas as pd

# ------------------------------
# Your original function (unchanged)
# ------------------------------
def load_file(data_url): 
    # Modify the URL to make it accessible for pandas
    modified_url = data_url.replace('/edit?usp=sharing', '/export?format=xlsx')

    # Load ALL sheets from the Excel file
    all_sheets = pd.read_excel(modified_url, sheet_name=None)

    data = {}

    # Loop through each sheet and store in dictionary
    for sheet_name, df in all_sheets.items():
        data[sheet_name] = df

    return data

# ------------------------------
# Streamlit App
# ------------------------------
st.title("Excel Loader Dashboard")

data_url = st.text_input("Enter Google Sheets Excel File URL")

if data_url:
    data = load_file(data_url)

    st.success("File loaded successfully!")
    st.write("Available sheets:", list(data.keys()))

    # Display a specific sheet (example: Switchbacks)
    if "Switchbacks" in data:
        st.subheader("Switchbacks Sheet Preview")
        st.dataframe(data["Switchbacks"])
    else:
        st.warning("'Switchbacks' sheet not found in the file.")
