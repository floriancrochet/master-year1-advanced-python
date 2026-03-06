# ECAP Store Dashboard
*This interactive Python dashboard monitors omnichannel retail sales performance and product frequencies.*

[ECAP Store Dashboard (Online)](https://master-year1-advanced-python.onrender.com)

---

## 🎯 Overview
This project provides tools for visualizing and monitoring key retail metrics, including sales evolution, product performance, and customer purchasing behavior.

**Objectives**
- Track total revenue and sales frequency by month
- Analyze top-selling products by gender
- Visualize weekly revenue trends
- Filter customer locations dynamically

---

## 🗄️ Data
- **Source:** `omnichannel_retail_line_items.csv`
- **Time Period / Size:** 52,955 rows
- **Preprocessing:** Handled missing values with zero-filling and computed total transaction prices
- **Data Availability:** Proprietary data provided in the `retail_insight_dashboard/` directory

---

## ⚙️ Features
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
uv run python retail_insight_dashboard/retail_insight_dashboard.py
```

---

## 📂 Project Structure

```text
retail_insight_dashboard/
│
├── README.md
├── omnichannel_retail_line_items.csv
└── retail_insight_dashboard.py
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
