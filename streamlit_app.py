import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # 시각화 라이브러리
import plotly.express as px
import plotly.graph_objects as go

# Title
st.title('■ Visualization_241005 ■')

st.write("")
st.write("")

# Subheader with custom margin
st.markdown(
    """
    <div style="margin-left: 50px; margin-right: 0px;">
        <h3>1. Streamlit for diverse forms of graph visualizations</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Pie chart
labels = ['A', 'B', 'C', 'D']
values = [300, 200, 100, 500]
fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])

# Bar chart
data_canada = px.data.gapminder().query("country == 'Canada'")
fig2 = px.bar(data_canada, x='year', y='pop', color='pop')

# Create two columns with 3:1 ratio
col1, col2 = st.columns([3, 1])

# First column with bar chart
with col1:
    st.plotly_chart(fig2, use_container_width=True)

# Second column with pie chart
with col2:
    st.plotly_chart(fig1, use_container_width=True)

# Scatter plot
df = px
