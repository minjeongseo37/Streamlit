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
fig1.update_layout(margin=dict(l=50, r=50, t=20, b=20))  # Pie chart margins

# Bar chart
data_canada = px.data.gapminder().query("country == 'Canada'")
fig2 = px.bar(data_canada, x='year', y='pop', color='pop')
fig2.update_layout(margin=dict(l=50, r=50, t=20, b=20))  # Bar chart margins


# Create two columns with 3:1 ratio
col1, col2 = st.columns([3, 1])

# First column with bar chart
with col1:
    st.plotly_chart(fig2, use_container_width=True)

# Second column with pie chart
with col2:
    st.plotly_chart(fig1, use_container_width=True)

# Scatter plot
df = px.data.gapminder()
fig3 = px.scatter(df.query("year == 2007"), x='gdpPercap', y='lifeExp', size='pop', color='continent')
fig3.update_layout(margin=dict(l=50, r=50, t=20, b=20))  # Scatter plot margins
st.plotly_chart(fig3)

st.write("")
st.write("")
st.write("")

# Second section with custom margin
st.markdown(
    """
    <div style="margin-left: 50px; margin-right: 0px;">
        <h3>2. Streamlit for sin and cos function visualization</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Sliders for sin and cos function visualization
x_start = st.slider('x 시작값', 0.0, 10.0, 0.0)
x_end = st.slider('x 끝값', 10.0, 20.0, 10.0)

x = np.linspace(x_start, x_end)

y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot sin and cos functions using Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(['sin', 'cos'])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('sin and cos function')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # Adjust margins
st.pyplot(fig)

# Expensive computation with caching
@st.cache
def expensive_computation(x):
    return np.sin(x) + np.cos(x)

result = expensive_computation(x)

st.markdown("</div>", unsafe_allow_html=True)
