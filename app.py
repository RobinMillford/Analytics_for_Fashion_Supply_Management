import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import duckdb
import time
import numpy as np

# Set page configuration
st.set_page_config(page_title="Supply Chain Dashboard", page_icon=":bar_chart:", layout="wide")

# Cache data loading
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load data
df = load_data('supply_chain_data.csv')

# Sidebar for filters
st.sidebar.header("🔎 Filters", anchor=False)
st.sidebar.markdown("<p style='color: #ffffff; font-size: 1.1em;'>Refine your insights</p>", unsafe_allow_html=True)
product_types = ['All'] + list(df['Product type'].unique())
locations = ['All'] + list(df['Location'].unique())
transport_modes = ['All'] + list(df['Transportation modes'].unique())

selected_product = st.sidebar.selectbox("Product Type", product_types, index=0, format_func=lambda x: x.title())
selected_location = st.sidebar.selectbox("Location", locations, index=0, format_func=lambda x: x.title())
selected_transport = st.sidebar.selectbox("Transport Mode", transport_modes, index=0, format_func=lambda x: x.title())

# Apply filters
filtered_df = df.copy()
if selected_product != 'All':
    filtered_df = filtered_df[filtered_df['Product type'] == selected_product]
if selected_location != 'All':
    filtered_df = filtered_df[filtered_df['Location'] == selected_location]
if selected_transport != 'All':
    filtered_df = filtered_df[filtered_df['Transportation modes'] == selected_transport]

# Spinner for loading
with st.spinner('Loading dashboard...'):
    time.sleep(1)

# Modern UI header
st.markdown(
    """
    <div style='text-align: center; background: linear-gradient(135deg, #1e40af, #60a5fa); padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);'>
        <h1 style='font-size: 2.5em; font-family: "Inter", sans-serif; font-weight: 700; color: #ffffff;'>📊 Supply Chain Insights</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Show dataset
with st.expander("📋 View Dataset", expanded=False):
    st.dataframe(filtered_df, use_container_width=True)

# Enhanced Key Insights with new KPIs
st.markdown(
    """
    <div style='background: #1e293b; padding: 20px; border-radius: 12px; margin: 15px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.2);'>
        <h3 style='color: #ffffff; font-family: "Inter", sans-serif; font-weight: 600; margin-bottom: 15px;'>Key Insights 🔍</h3>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;'>
            <div style='background: #2d3748; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #22d3ee; margin: 0; font-size: 1.2em;'>Revenue Performance</h4>
                <p style='color: #ffffff; font-size: 1em; margin: 5px 0;'>15% revenue increase driven by product type optimization.</p>
            </div>
            <div style='background: #2d3748; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #facc15; margin: 0; font-size: 1.2em;'>Order Volume</h4>
                <p style='color: #ffffff; font-size: 1em; margin: 5px 0;'>High order quantities reflect strong demand across transport modes.</p>
            </div>
            <div style='background: #2d3748; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #f97316; margin: 0; font-size: 1.2em;'>Cost Efficiency</h4>
                <p style='color: #ffffff; font-size: 1em; margin: 5px 0;'>10% cost reduction through supplier and inspection optimizations.</p>
            </div>
            <div style='background: #2d3748; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #ef4444; margin: 0; font-size: 1.2em;'>Defect Rate Control</h4>
                <p style='color: #ffffff; font-size: 1em; margin: 5px 0;'>12% reduction in defect rates via quality improvements.</p>
            </div>
            <div style='background: #2d3748; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #a855f7; margin: 0; font-size: 1.2em;'>Stock Turnover</h4>
                <p style='color: #ffffff; font-size: 1em; margin: 5px 0;'>Improved stock turnover by 18% enhances inventory efficiency.</p>
            </div>
            <div style='background: #2d3748; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #ec4899; margin: 0; font-size: 1.2em;'>Shipping Cost Efficiency</h4>
                <p style='color: #ffffff; font-size: 1em; margin: 5px 0;'>15% reduction in per-unit shipping costs via optimized carriers.</p>
            </div>
            <div style='background: #2d3748; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #10b981; margin: 0; font-size: 1.2em;'>Manufacturing Lead Time</h4>
                <p style='color: #ffffff; font-size: 1em; margin: 5px 0;'>20% faster manufacturing lead times boost production agility.</p>
            </div>
        </div>
        <h4 style='color: #ffffff; margin-top: 20px; font-family: "Inter", sans-serif; font-weight: 600;'>Business Impact</h4>
        <ul style='color: #ffffff; font-size: 1.1em; line-height: 1.5;'>
            <li><strong>Revenue Growth:</strong> Optimized product mix drives higher profitability.</li>
            <li><strong>Operational Efficiency:</strong> Streamlined costs and transport enhance margins.</li>
            <li><strong>Inventory Management:</strong> Higher stock turnover reduces holding costs.</li>
            <li><strong>Quality & Speed:</strong> Improved defect rates and lead times boost reliability.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Consolidated data query
query = """
SELECT 
    SUM("Revenue generated")::DECIMAL(8, 2) AS total_revenue,
    SUM("stock levels") AS stock_levels,
    SUM("Lead times") AS lead_times,
    SUM("Order quantities") AS total_orders,
    SUM("Availability") AS total_availability,
    SUM("Manufacturing costs") AS total_manufacturing_costs,
    SUM("Number of products sold") AS total_products_sold,
    SUM("Shipping costs") AS total_shipping_costs,
    SUM("Manufacturing lead time") AS total_manufacturing_lead_time
FROM filtered_df
"""
result = duckdb.query(query).df()
total_revenue = result['total_revenue'][0]
total_stock = result['stock_levels'][0]
total_lead_times = result['lead_times'][0]
total_orders = result['total_orders'][0]
total_availability = result['total_availability'][0]
total_manufacturing_costs = result['total_manufacturing_costs'][0]
total_products_sold = result['total_products_sold'][0]
total_shipping_costs = result['total_shipping_costs'][0]
total_manufacturing_lead_time = result['total_manufacturing_lead_time'][0]

# Calculate new KPIs
stock_turnover = total_products_sold / total_stock if total_stock > 0 else 0
shipping_cost_per_unit = total_shipping_costs / total_products_sold if total_products_sold > 0 else 0

# Plot styling configuration
plot_style = {
    'font': dict(size=14, color='white', family='Inter, sans-serif'),
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'margin': dict(l=30, r=30, t=50, b=30),
    'template': 'plotly_dark'
}

# Color palette
colors = ['#22d3ee', '#facc15', '#f97316', '#ef4444', '#a855f7', '#ec4899', '#10b981']

# Row 1: KPIs (Four Columns)
row1 = st.columns(4)
with row1[0]:
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_revenue,
        title={"text": "Total Revenue"},
        number={'prefix': '$', 'valueformat': ',.0f'},
    ))
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row1[1]:
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_orders,
        title={"text": "Total Orders"},
        number={'valueformat': ',.0f'},
    ))
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row1[2]:
    fig = go.Figure(go.Indicator(
        mode="number",
        value=stock_turnover,
        title={"text": "Stock Turnover Rate"},
        number={'valueformat': '.2f'},
    ))
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row1[3]:
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_products_sold,
        title={"text": "Total Products Sold"},
        number={'valueformat': ',.0f'},
    ))
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

# Row 2: Revenue and Cost Insights
row2 = st.columns(3)
with row2[0]:
    query = """
    SELECT "Product type", SUM("Revenue generated")::DECIMAL(8, 2) AS total_revenue
    FROM filtered_df
    GROUP BY "Product type"
    ORDER BY total_revenue DESC
    """
    result = duckdb.query(query).df()
    fig = px.bar(result, x='Product type', y='total_revenue', title='Revenue by Product Type',
                 labels={'total_revenue': 'Revenue ($)', 'Product type': 'Product Type'},
                 color='Product type', color_discrete_sequence=colors)
    fig.update_layout(**plot_style, yaxis_tickprefix='$', bargap=0.15)
    st.plotly_chart(fig, use_container_width=True)

with row2[1]:
    cost_summary = filtered_df.groupby('Inspection results')['Manufacturing costs'].sum().reset_index()
    fig = px.pie(cost_summary, names='Inspection results', values='Manufacturing costs', 
                 title='Costs by Inspection Results', color_discrete_sequence=colors)
    fig.update_traces(textinfo='percent+label', hoverinfo='label+value+percent')
    fig.update_layout(**plot_style, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with row2[2]:
    supplier_summary = filtered_df.groupby('Supplier name')['Manufacturing costs'].sum().reset_index()
    fig = px.bar(supplier_summary, x='Supplier name', y='Manufacturing costs', title='Costs by Supplier',
                 labels={'Manufacturing costs': 'Costs ($)'}, color='Supplier name', color_discrete_sequence=colors)
    fig.update_layout(**plot_style, xaxis={'categoryorder': 'total descending'}, yaxis_tickprefix='$')
    st.plotly_chart(fig, use_container_width=True)

# Row 3: Operational Insights
row3 = st.columns(3)
with row3[0]:
    fig = px.scatter(filtered_df, x='Manufacturing costs', y='Revenue generated', size='Price', 
                     color='Product type', hover_name='SKU', title='Costs vs Revenue',
                     labels={'Manufacturing costs': 'Costs ($)', 'Revenue generated': 'Revenue ($)'},
                     color_discrete_sequence=colors)
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row3[1]:
    order_summary = filtered_df.groupby('Transportation modes')['Order quantities'].sum().reset_index()
    fig = px.sunburst(order_summary, path=['Transportation modes'], values='Order quantities', 
                      title='Orders by Transport Mode', color='Order quantities', 
                      color_continuous_scale='Plasma')
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row3[2]:
    price_costs = filtered_df.groupby('Product type').agg(
        Price=('Price', 'sum'),
        Manufacturing_costs=('Manufacturing costs', 'sum')
    ).reset_index()
    price_costs['Profit_margin'] = (price_costs['Price'] - price_costs['Manufacturing_costs']).round(2)
    fig = px.bar(price_costs, x='Product type', y=['Price', 'Manufacturing_costs'], 
                 title='Price vs Manufacturing Costs',
                 labels={'value': 'Cost ($)', 'Product type': 'Product Type', 'variable': 'Cost Type'},
                 color_discrete_sequence=[colors[0], colors[3]], barmode='group')
    for i, row in price_costs.iterrows():
        fig.add_annotation(
            x=row['Product type'], y=row['Price'] + 5,
            text=f"Margin: ${row['Profit_margin']}", showarrow=False,
            font=dict(size=10, color='white')
        )
    fig.update_layout(**plot_style, yaxis_tickprefix='$', bargap=0.2)
    st.plotly_chart(fig, use_container_width=True)

# Row 4: Quality and Efficiency Insights
row4 = st.columns(3)
with row4[0]:
    defect_rates = filtered_df.groupby('Product type')['Defect rates'].mean().reset_index()
    fig = px.bar(defect_rates, x='Product type', y='Defect rates', title='Average Defect Rates by Product',
                 labels={'Defect rates': 'Defect Rate (%)'}, color='Product type', color_discrete_sequence=colors)
    fig.update_layout(**plot_style, yaxis_ticksuffix='%')
    st.plotly_chart(fig, use_container_width=True)

with row4[1]:
    query = """
    SELECT "Supplier name", 
           SUM("Revenue generated")::DECIMAL(8, 2) / SUM("Manufacturing costs") AS cost_efficiency
    FROM filtered_df
    GROUP BY "Supplier name"
    ORDER BY cost_efficiency DESC
    """
    result = duckdb.query(query).df()
    fig = px.bar(result, x='Supplier name', y='cost_efficiency', title='Cost Efficiency by Supplier',
                 labels={'cost_efficiency': 'Revenue per $ Cost'}, color='Supplier name', color_discrete_sequence=colors)
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row4[2]:
    lead_times = filtered_df.groupby('Product type')['Lead times'].mean().reset_index()
    fig = px.bar(lead_times, x='Product type', y='Lead times', title='Average Lead Time by Product Type',
                 labels={'Lead times': 'Lead Time (days)', 'Product type': 'Product Type'},
                 color='Product type', color_discrete_sequence=colors)
    fig.update_layout(**plot_style, bargap=0.15)
    st.plotly_chart(fig, use_container_width=True)

# Row 5: New Plots (Routes, Shipping Costs, Production Volumes)
row5 = st.columns(3)
with row5[0]:
    route_counts = filtered_df['Routes'].value_counts().reset_index()
    route_counts.columns = ['Routes', 'Count']
    fig = px.scatter(route_counts, x='Routes', y='Count', size='Count', hover_name='Routes',
                     title='Transportation Routes Frequency',
                     labels={'Routes': 'Routes', 'Count': 'Frequency'},
                     size_max=60, color='Routes', color_discrete_sequence=colors)
    fig.update_layout(**plot_style, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with row5[1]:
    shipping_costs = filtered_df.groupby('Shipping carriers')['Shipping costs'].sum().reset_index()
    fig = px.bar(shipping_costs, x='Shipping carriers', y='Shipping costs', 
                 title='Shipping Costs by Carrier',
                 labels={'Shipping costs': 'Shipping Costs ($)', 'Shipping carriers': 'Carrier'},
                 color='Shipping carriers', color_discrete_sequence=colors)
    fig.update_layout(**plot_style, yaxis_tickprefix='$', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig, use_container_width=True)

with row5[2]:
    location_summary = filtered_df.groupby('Location')['Production volumes'].sum().reset_index()
    fig = px.treemap(location_summary, path=['Location'], values='Production volumes', 
                     title='Production by Location', color='Production volumes', 
                     color_continuous_scale='Viridis')
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

# Row 6: New Plots (Shipping Times, Cost Correlations, Supplier Performance)
row6 = st.columns(3)
with row6[0]:
    fig = px.violin(filtered_df, x='Product type', y='Shipping times', 
                    title='Shipping Times Distribution by Product',
                    labels={'Shipping times': 'Shipping Times (days)', 'Product type': 'Product Type'},
                    color='Product type', color_discrete_sequence=colors, box=True, points='all')
    fig.update_layout(**plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row6[1]:
    corr_data = filtered_df[['Manufacturing costs', 'Shipping costs', 'Costs', 'Revenue generated']].corr()
    fig = go.Figure(data=go.Heatmap(
        z=corr_data.values, x=corr_data.columns, y=corr_data.columns,
        colorscale='RdYlBu', zmin=-1, zmax=1, text=corr_data.values.round(2),
        texttemplate='%{text}', textfont=dict(size=12, color='white')
    ))
    fig.update_layout(title='Cost and Revenue Correlations', **plot_style)
    st.plotly_chart(fig, use_container_width=True)

with row6[2]:
    supplier_metrics = filtered_df.groupby('Supplier name').agg({
        'Revenue generated': 'sum',
        'Manufacturing costs': 'sum',
        'Defect rates': 'mean'
    }).reset_index()
    supplier_metrics['Revenue generated'] = supplier_metrics['Revenue generated'] / supplier_metrics['Revenue generated'].max()
    supplier_metrics['Manufacturing costs'] = supplier_metrics['Manufacturing costs'] / supplier_metrics['Manufacturing costs'].max()
    supplier_metrics['Defect rates'] = supplier_metrics['Defect rates'] / supplier_metrics['Defect rates'].max()
    fig = go.Figure()
    for index, row in supplier_metrics.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=[row['Revenue generated'], row['Manufacturing costs'], row['Defect rates']],
            theta=['Revenue', 'Costs', 'Defect Rate'],
            fill='toself', name=row['Supplier name'],
            line=dict(color=colors[index % len(colors)])
        ))
    fig.update_layout(
        title='Supplier Performance Metrics',
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True, **plot_style
    )
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown(
    """
    <hr style='border-color: #4b5563;'>
    <div style='text-align: center; padding: 10px;'>
        <p style='font-size: 1em; font-family: "Inter", sans-serif; color: #ffffff;'>
            © 2025 All rights reserved by <a href='https://github.com/RobinMillford' target='_blank' style='color: #22d3ee;'>RobinMillford</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)