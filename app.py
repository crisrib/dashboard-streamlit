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

st.title("Welcome to NFL Offensive Dashboard") # Title of the Website
st.subheader("NFL Passing,Rushing,Recieving Yards from 09-2019 to 11-2022 ") # Subheader

# Importing Dataframe
st.header("This is the dataframe")
def load_data (nrows):
    df = pd.read_excel('data/nfl_pass_rush_receive_raw_data.xls', nrows=nrows)
    lowercase = lambda x:str(x).title()
    df.rename (lowercase, axis='columns',inplace=True)
    return df
    
df = load_data (100)
list(df.columns)

#Example code of a show and hide checkbox

if st.checkbox('Show dataframe'):
    chart_data = AgGrid(df)


# Clean data for filtering 
 
df.columns = df.columns.str.replace(' ', '_')

#SideBar Panel
st.sidebar.header("Please Select Filter Here:")

Pos = st.sidebar.multiselect(
    "Select the Position",
    options=df['Pos'].unique(),
    default=df['Pos'].unique()
)
Team = st.sidebar.multiselect(
    "Select the Team",
    options=df['Team'].unique(),
    default=df['Team'].unique()
)
Player = st.sidebar.multiselect(
    "Select the Player",
    options=df['Player'].unique(),
    default=df['Player'].unique()
)



df_selection = df.query(
    "Player == @Player & Team == @Team & Pos == @Pos"

)
st.title("Filtered dataframe by Sidebar")
st.dataframe(df_selection)


st.bar_chart(data=df,x='Player',y='Pass_Yds', width=0, height=0, use_container_width=True)


st.line_chart(data=df, y='Pass_Sacked', x='Team', width=0, height=0, use_container_width=True)