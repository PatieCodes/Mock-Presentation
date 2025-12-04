import streamlit as st
import pandas as pd

def load_file(data_url: str):
    """
    Loads all sheets from an Excel file stored on Google Drive
    and returns a dictionary of DataFrames.
    """

    # Convert Google Drive "edit" link → direct download link
    modified_url = data_url.replace("/edit?usp=sharing", "/export?format=xlsx")

    try:
        all_sheets = pd.read_excel(modified_url, sheet_name=None)
    except Exception as e:
        st.error(f"Failed to load the file: {e}")
        return None

    return all_sheets


# --- Streamlit App Section ---
st.title("Excel Data Loader Dashboard")

data_url = st.text_input(
    "Enter Google Drive Excel File URL",
    placeholder="Paste your Google Drive link here..."
)

if data_url:
    data = load_file(data_url)

    if data:
        st.success("File loaded successfully!")

        # Show list of sheets
        sheet = st.selectbox("Select sheet to view:", list(data.keys()))

        # Display sheet content
        st.subheader(f"Preview of: {sheet}")
        st.dataframe(data[sheet])

