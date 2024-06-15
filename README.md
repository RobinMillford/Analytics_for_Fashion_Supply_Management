---

# Supply Chain Analysis Dashboard

## Overview

This Streamlit dashboard provides a comprehensive analysis of supply chain data, focusing on key metrics such as production volumes, stock levels, order quantities, revenue, manufacturing costs, lead times, shipping costs, transportation routes, risk factors, and sustainability factors. The interactive visualizations allow for an in-depth understanding of the supply chain's performance and highlight areas for improvement.

## Features

- **Total Production Volumes, Stock Levels, and Lead Times**: Displays total values for production volumes, stock levels, and lead times with indicators.
- **Revenue Distribution by Location**: A pie chart showing revenue distribution across different locations.
- **Manufacturing Costs by Supplier**: Bar chart displaying the distribution of manufacturing costs by supplier.
- **Comparison of Price and Manufacturing Costs by Product Type**: Bar chart comparing the prices and manufacturing costs for different product types, along with profit margins.
- **Relationship between Production Volume, Stock Levels, and Order Quantities**: Polar chart illustrating the relationship between key supply chain metrics.
- **Distribution of Shipping Costs by Shipping Carriers**: Bar chart depicting the distribution of shipping costs among different shipping carriers.
- **Average Lead Time by Product Type**: Bar chart showing the average lead time for different product types.
- **Transportation Routes and Their Frequency**: Bubble chart representing the frequency of various transportation routes.
- **Supply Chain Risk Distribution by Risk Factors**: Bar chart showing the distribution of supply chain risks by different risk factors.
- **Sustainability Factors in the Supply Chain**: Pie chart analyzing the sustainability factors in the supply chain.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RobinMillford/Analytics_for_Fashion_Supply_Management.git
   cd Analytics_for_Fashion_Supply_Management
   ```

2. **Install Dependencies**
   Ensure you have Python installed. It's recommended to use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Dashboard Locally**
   ```bash
   streamlit run app.py
   ```

## Deployment

The dashboard is deployed on Streamlit Cloud. You can access it [here](https://analyticsforfashionsupplymanagement.streamlit.app/).

## Data

Ensure that the data file `supply_chain_data.csv` is in the correct format and located in the appropriate directory as expected by the dashboard script.

[Dataset](https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
