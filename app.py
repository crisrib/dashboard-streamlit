import streamlit as st
import numpy as np
import pandas as pd
from streamlit_folium import folium_static
import folium
import streamlit.components.v1 as components
import numpy as np
from st_aggrid import AgGrid

# Page Setting
st.set_page_config(layout='wide')

# Title of the Website
st.title("Leading Causes of Death")
# Subheader
st.subheader("United States report from 1999 to 2017 ")

# Importing Dataframe
st.header("Data")   
def load_data (nrows):
    df = pd.read_excel('data/LCODUSdata.cvs.csv', nrows=nrows)
    lowercase = lambda x:str(x).title()
    df.rename (lowercase, axis='columns',inplace=True)
    return df
    
df = load_data (100)
list(df.columns)

# Clean data for filtering 
df.columns = df.columns.str.replace(' ', '_')

# Show and hide checkbox
if st.checkbox('Show dataframe'):
    chart_data = AgGrid(df)

#SideBar Panel
st.sidebar.header("Please Select Filter Here:")

Cause = st.sidebar.multiselect(
    "Select the Cause",
    options=df['Cause'].unique(),
    default=df['Cause'].unique()
)
State = st.sidebar.multiselect(
    "Select the State",
    options=df['State'].unique(),
    default=df['State'].unique()
)
Year = st.sidebar.multiselect(
    "Select the Year",
    options=df['Year'].unique(),
    default=df['Year'].unique()
)


df_selection = df.query(
    "Cause == @Cause & State == @State & Year == @Year"

)
st.title("Filtered dataframe by Sidebar")
st.dataframe(df_selection)

st.bar_chart(data=df,x='State',y='Deaths', width=0, height=0, use_container_width=True)

st.line_chart(data=df, y='Cause', x='Deaths', width=0, height=0, use_container_width=True)