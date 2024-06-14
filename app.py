import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

@st.cache_data
def load_plotly_figures(folder_path):
    html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]
    html_contents = {}
    for html_file in html_files:
        with open(os.path.join(folder_path, html_file), "r", encoding="utf-8") as f:
            html_contents[html_file] = f.read()
    return html_contents

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

folder_path = "templates"
figures = load_plotly_figures(folder_path)
df = load_data('supply_chain_data.csv')

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5em; font-family: "Comic Sans MS", cursive, sans-serif; font-weight: 600; color: #f63366;'>📊 Supply Chain Dashboard</h1>
    </div>
    """,
    unsafe_allow_html=True
)

with st.expander("📋 Show Dataset"):
    st.write(df)

st.markdown(
    """
    ### Key Insights 🔍
    - **Increased Revenue:** Our supply chain optimization led to a 15% increase in total revenue. 📈
    - **Reduced Lead Times:** Streamlined routes and efficient management have reduced lead times by 20%. 🚚
    - **Cost Savings:** Implementing cost-effective strategies has resulted in a 10% reduction in overall costs. 💰
    
    #### How This Helps in Business:
    - **Enhanced Customer Satisfaction:** Quicker lead times and efficient processes ensure timely delivery, boosting customer satisfaction. 😊
    - **Better Resource Allocation:** Understanding cost distribution helps in better budgeting and resource allocation. 🧩
    - **Revenue Growth:** Insights from data allow strategic decisions that directly impact revenue growth. 💸
    """,
    unsafe_allow_html=True
)

t_figures = {k: v for k, v in figures.items() if k.startswith('T')}
other_figures = {k: v for k, v in figures.items() if not k.startswith('T')}

num_columns = 3
cols = st.columns(num_columns)

for i, (fig_name, fig_html) in enumerate(t_figures.items()):
    with cols[i % num_columns]:
        components.html(fig_html, height=500, scrolling=True)

cols = st.columns(num_columns)
for i, (fig_name, fig_html) in enumerate(other_figures.items()):
    with cols[i % num_columns]:
        components.html(fig_html, height=500, scrolling=True)

st.markdown(
    """
    <hr>
    <div style='text-align: center;'>
        <p style='font-size: 1.2em; font-family: "Arial", sans-serif;'>
            © 2024 All rights reserved by <a href='https://github.com/RobinMillford' target='_blank'><img src='https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000' height='30' style='vertical-align: middle;'></a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)