import streamlit as st
import pandas as pd
import plotly.express as px
import os
import json

st.set_page_config(page_title="TMM Financial Categorizor", page_icon="$", layout="wide")
category_file = "categories.json"

if "categories" not in st.session_state:
  st.session_state.categories = {
      "Uncategorized":[]
  }
if os.path.exists(category_file):
  with open(category_file, "r") as f:
    st.session_state.categories = json.load(f)

def save_categories():
  with open(category_file, "w") as f:
    json.dump(st.session_state.categories, f)

def load_transactions(file):
  try: 
    df = pd.read_csv(file)
    df.columns = [col.strip() for col in df.columns]
    df["Amount"] = df["Amount"].str.replace(",","").astype(float)
    df["Date"] = pd.to_datetime(df["date"], format="%d %b %Y")
  except Exception as e:
    st.error(f"Error processing file: {str(e)}")

def main():
  st.title("TMM Financial Categorizor")
  uploaded_file = st.file_uploader("Upload transactions CSV", type=["csv"])

  if uploaded_file is not None:
    df = load_transactions(uploaded_file)

main()