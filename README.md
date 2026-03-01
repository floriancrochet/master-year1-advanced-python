# Supermarket & ECAP Store Dashboards
*Explore retail sales data through two interactive Dash analytical dashboards.*

[Supermarket Sales Dashboard (Live)](https://master-year1-advanced-python-1.onrender.com) | [ECAP Store Dashboard (Live)](https://master-year1-advanced-python.onrender.com)

---

## 🎯 Overview
This project provides two interactive dashboards built with Dash to analyze and visualize retail sales data from supermarket and omnichannel retail datasets.

**Objectives**
- Visualize sales performance and key indicators through dynamic dashboards
- Enable interactive filtering by gender, city, and customer location
- Aggregate and display product category distributions and revenue trends
- Support operational monitoring through weekly purchase and revenue evolution charts

---

## 🗄️ Data
- **Source:** Local CSV files bundled in the repository
- **Key Predictors / Features:** Gender, City/Location, Product_Category, Quantity, Avg_Price, Discount_pct, Total, Date
- **Preprocessing:** Column renaming to French labels, datetime parsing, revenue computation (Quantity * Avg_Price * discount factor)
- **Data Availability:** Included in the repository under `supermarket_sales_dashboard/` and `retail_insight_dashboard/`

---

## ⚙️ Features

### Supermarket Sales Dashboard
- **Display Total Purchase Amount:** Aggregate indicator of total sales in USD
- **Count Total Purchases:** Unique invoice count indicator
- **Plot Purchase Distribution:** Histogram of purchase amounts segmented by gender and city
- **Visualize Product Categories:** Pie chart of product category distribution
- **Track Weekly Purchase Evolution:** Line chart of weekly total purchases by city
- **Filter by Gender and City:** Multi-select dropdown filters for gender and city

### ECAP Store Dashboard
- **Display Monthly Revenue Indicator:** Revenue indicator with month-over-month delta comparison
- **Show Monthly Sales Frequency:** Sales count indicator with delta comparison
- **Rank Top 10 Products:** Horizontal bar chart of best-selling products by gender
- **Plot Weekly Revenue Evolution:** Line chart of weekly revenue trends
- **Filter by Customer Location:** Multi-select dropdown filter by customer location
- **List Recent Sales:** Interactive paginated table of the 100 most recent transactions

---

## 🧰 Tech Stack
- **Language:** Python 3.10+
- **Data Manipulation:** pandas, NumPy
- **Visualization:** Plotly, Dash, Dash Bootstrap Components
- **Deployment & MLOps:** gunicorn

---

## 📦 Installation

```bash
git clone https://github.com/floriancrochet/master-year1-advanced-python.git
cd master-year1-advanced-python
uv sync
```

---

## 💻 Usage Example

### Reproducing the Analysis / Execution Pipeline

```bash
uv run python supermarket_sales_dashboard/supermarket_sales_dashboard.py
```

```bash
uv run python retail_insight_dashboard/retail_insight_dashboard.py
```

---

## 📂 Project Structure

```text
master-year1-advanced-python/
│
├── supermarket_sales_dashboard/
│   ├── supermarket_sales_dashboard.py          # Supermarket sales Dash application
│   ├── supermarket_sales.csv                   # Supermarket transactions dataset
│   └── README.md                               # Supermarket dashboard documentation
├── retail_insight_dashboard/
│   ├── retail_insight_dashboard.py             # ECAP store Dash application
│   ├── omnichannel_retail_line_items.csv       # Omnichannel retail dataset
│   └── README.md                               # ECAP dashboard documentation
├── main.py                                     # Entry point placeholder
├── pyproject.toml                              # Python dependencies & project config (uv)
├── uv.lock                                     # Exact Python dependency tree (uv)
├── LICENSE                                     # MIT License
├── .gitignore                                  # Git ignore rules
└── README.md                                   # Project documentation
```

---

## 📈 Results

*(The application functions primarily as an interactive exploratory dashboard. No explicit predictive performance metrics were formulated).*

---

## 📜 License
This project is released under the MIT License.
© 2025 Florian Crochet

---

## 👤 Author
**Florian Crochet**
[GitHub Profile](https://github.com/floriancrochet)

*Master 1 – Econometrics & Statistics, Applied Econometrics Track*

---

## 🤝 Acknowledgments
This work was conducted as part of the Advanced Python module, supervised by M. Abdoul Razac SANE.
