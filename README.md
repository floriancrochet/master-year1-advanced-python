# Supermarket & ECAP Store Dashboards
*Explore retail sales data through two interactive Dash analytical dashboards.*

| Sub-Project | Description |
| :--- | :--- |
| [Supermarket Sales Dashboard (Online)](https://master-year1-advanced-python-1.onrender.com) | Provide a visual and interactive analysis of supermarket sales |
| [ECAP Store Dashboard (Online)](https://master-year1-advanced-python.onrender.com) | Track total revenue and sales frequency by month |

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
- **Source:** `supermarket_sales.csv` and `omnichannel_retail_line_items.csv`
- **Time Period / Size:** 1,000 rows (Supermarket), 52,955 rows (ECAP)
- **Preprocessing:** Translated columns and modalities to French, converted dates, handled missing values with zero-filling, and computed total transaction prices
- **Data Availability:** Included in the repository under `supermarket_sales_dashboard/` and `retail_insight_dashboard/`

---

## ⚙️ Features

### Supermarket Sales Dashboard
- **Calculate Totals:** Provide dynamic purchase amount and transaction indicators
- **Visualize Histograms:** Display interactive total amounts segmented by gender and city
- **Plot Distributions:** Generate a pie chart detailing product category market shares
- **Track Evolution:** Draw line charts to monitor weekly sales progress by city
- **Translate Interface:** Implement full French localization for columns and modalities
- **Enable Interactivity:** Apply real-time Dash callbacks for dynamic filtering

### ECAP Store Dashboard
- **Visualize Retail Data:** Display revenue and product sales frequency using Plotly charts
- **Track Weekly Revenue:** Map weekly sales evolution through interactive line graphs
- **Analyze Product Frequency:** Extract the top 10 best-selling products categorized by gender
- **Compute Real-Time Indicators:** Calculate monthly revenue totals dynamically
- **Filter Dashboard Modules:** Slice the entire application instantaneously by store location
- **Explore Sales History:** Present the 100 most recent transactions within an interactive table

---

## 🧰 Tech Stack
- **Language:** Python 3.10+
- **Numerical Computing & Data Manipulation:** pandas, NumPy
- **Data Visualization:** Plotly
- **Dashboards & Web APIs:** Dash, Dash Bootstrap Components, gunicorn

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
│   ├── supermarket_sales_dashboard.py        # Supermarket sales Dash application
│   ├── supermarket_sales.csv                 # Supermarket transactions dataset
│   └── README.md                             # Supermarket dashboard documentation
├── retail_insight_dashboard/
│   ├── retail_insight_dashboard.py           # ECAP store Dash application
│   ├── omnichannel_retail_line_items.csv     # Omnichannel retail dataset
│   └── README.md                             # ECAP dashboard documentation
├── pyproject.toml                            # Python dependencies & project config (uv)
├── uv.lock                                   # Exact Python dependency tree (uv)
├── LICENSE                                   # MIT License
├── .gitignore                                # Git ignore rules
└── README.md                                 # Project documentation
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
