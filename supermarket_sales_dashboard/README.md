# Supermarket Sales Dashboard
*This project provides an interactive Dash application for exploring supermarket sales by gender and city.*

[Supermarket Sales Dashboard (Online)](https://master-year1-advanced-python-1.onrender.com)

---

## 🎯 Overview
This project provides an interactive dashboard built with Dash to analyze supermarket sales data.

**Objectives**
- Provide a visual and interactive analysis of supermarket sales
- Allow filtering by gender and city
- Display dynamic indicators and graphs for decision support

---

## 🗄️ Data
- **Source:** `supermarket_sales.csv`
- **Time Period / Size:** 1,000 rows
- **Preprocessing:** Translated columns and modalities to French, converted dates
- **Data Availability:** Provided in the `supermarket_sales_dashboard/` directory

---

## ⚙️ Features
- **Calculate Totals:** Provide dynamic purchase amount and transaction indicators
- **Visualize Histograms:** Display interactive total amounts segmented by gender and city
- **Plot Distributions:** Generate a pie chart detailing product category market shares
- **Track Evolution:** Draw line charts to monitor weekly sales progress by city
- **Translate Interface:** Implement full French localization for columns and modalities
- **Enable Interactivity:** Apply real-time Dash callbacks for dynamic filtering

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

---

## 📂 Project Structure

```text
supermarket_sales_dashboard/
│
├── README.md
├── supermarket_sales.csv
└── supermarket_sales_dashboard.py
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
