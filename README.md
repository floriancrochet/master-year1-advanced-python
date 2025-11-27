# Supermarket & ECAP Store Dashboards  
*Interactive Dash applications for retail sales analysis and performance monitoring.*

---

## 🌐 Live Dashboards
Access the deployed dashboards directly:

- **Supermarket Sales Dashboard**: https://master-year1-advanced-python-1.onrender.com  
- **ECAP Store Dashboard**: https://master-year1-advanced-python.onrender.com

---

## 📘 Overview
This project consists of two analytical dashboards developed with **Dash** to explore and visualize retail sales data:

- **Supermarket Sales Dashboard**: focuses on analyzing supermarket transactions by gender and city.
- **ECAP Store Dashboard**: provides insights into omnichannel retail performance, including revenue trends and product performance.

Both applications aim to deliver clear, interactive decision-support tools for sales analysis and operational monitoring.

**Objectives**
- Visualize and analyze sales performance through dynamic dashboards
- Enable interactive filtering for targeted analysis
- Provide key performance indicators for strategic insights
- Support data-driven decision-making through graphical summaries

---

## ⚙️ Features

### Supermarket Sales Dashboard
- Total purchase amount indicator (sum of total sales)
- Total number of purchases indicator (unique invoices)
- Interactive histogram of total purchase amounts by gender and city
- Pie chart showing product category distribution
- Weekly evolution line chart of total purchases by city
- Filters by gender and city
- French-translated interface for data display

### ECAP Store Dashboard
- Monthly revenue indicator with delta comparison
- Monthly sales frequency indicator
- Top 10 best-selling products by gender
- Weekly revenue evolution chart
- Dynamic filtering by customer location
- Interactive table of the 100 most recent sales

---

## 🧰 Tech Stack
**Language:** Python  
**Libraries:** Dash, Plotly, Dash Bootstrap Components, pandas, NumPy

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/<project-name>.git
cd <project-name>
pip install -r requirements.txt
```

> À compléter

---

## 📚 Usage Example

### Supermarket Sales Dashboard
```bash
python app.py
```
Open your browser at: `http://localhost:8000`

### ECAP Store Dashboard
```bash
python app.py
```
Open your browser at: `http://127.0.0.1:8100/`

Deployed versions:
- Supermarket Sales Dashboard: https://master-year1-advanced-python-1.onrender.com
- ECAP Store Dashboard: https://master-year1-advanced-python.onrender.com

---

## 📂 Project Structure

```
project-root/
│
├── supermarket_sales_dashboard/
│   └── supermarket_sales.csv
├── retail_insight_dashboard/
│   └── omnichannel_retail_line_items.csv
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Results
The dashboards present interactive visualizations, including:
- Key performance indicators (sales, revenue, purchase frequency)
- Product category distributions
- Weekly trends in purchases and revenue
- Filtered views by demographic and geographic criteria

> À compléter

---

## 🧠 References
- Supermarket dataset: `supermarket_sales.csv`
- Omnichannel retail dataset: `omnichannel_retail_line_items.csv`
- Python-Dash Course – Master 1 ECAP (2024–2025)
- Plotly Dash Documentation
- Dash Bootstrap Components Guide

---

## 📜 License
This project is released under the **MIT License**.  
© 2025 Florian Crochet

---

## 👤 Author
**Florian Crochet**  
[GitHub Profile](https://github.com/floriancrochet)

*Master 1 – Econometrics & Statistics, Applied Econometrics Track*

---

## 💬 Acknowledgments
Developed as part of the Python-Dash academic project under the supervision of **M. Abdoul Razac SANE**.  
Thanks to the open-source Dash and Plotly communities for their excellent tools and documentation.

