import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # 시각화 라이브러리
import plotly.express as px

def main_page():
    st.title('Main Page🎈')
    st.sidebar.title('Side Main🎈')
    
def page2():
    st.title('Page 2📒')
    st.sidebar.title('Side 2📒')
    st.header('1-2. Streamlit for sin and cos function visualization')

x_start = st.slider('x 시작값' ,  0.0, 10.0, 0.0)
x_end = st.slider('x 시작값' ,  10.0, 20.0, 10.0)


x = np.linspace(x_start, x_end)

y_sin = np.sin(x)
y_cos = np.cos(x)


fig , ax = plt.subplots()

ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(['sin', 'cos'])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.set_title('sin and cos fuction')

st.pyplot(fig)

@st.cache
def expensive_computataion(x):
    return np.sin(x) + np.cos(x)

result = expensive_computataion(x)



def page3():
    st.title('Page 3🎉')
    st.sidebar.title('Side 3🎉')

page_names = {'Main Page': main_page, 'Page 2':page2, 'Page 3':page3}
    
selected_page = st.sidebar.selectbox('Select a page', page_names.keys())
page_names[selected_page]()


st.title('1. Visualization_241005')

st.header('1-2. Streamlit for diverse forms of graph visualizations')

import plotly.graph_objects as go
labels = ['A','B','C','D']
values = [300,200,100,500]
fig1 = go.Figure(data = [go.Pie(labels = labels, values = values, hole =.3)])

import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig2 = px.bar(data_canada, x='year', y='pop', color = 'pop')

# Create two columns with 3:1 ratio
col1, col2 = st.columns([3, 1])  # col1은 col2의 절반 너비 열 생성

# First column with pie chart
with col1:
    st.plotly_chart(fig2, use_container_width=True)  # 바 차트 출력  

# Second column with bar chart and image
with col2:
    st.plotly_chart(fig1, use_container_width=True)  # 파이 차트 출력


df = px.data.gapminder()
fig3 = px.scatter(df.query("year == 2007"), x = 'gdpPercap' , y = 'lifeExp', size = 'pop', color = 'continent')
st.plotly_chart(fig3)


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")






