# Supermarket Sales Dashboard  
*An interactive Dash application for exploring supermarket sales by gender and city.*

[**Supermarket Sales Dashboard**](https://master-year1-advanced-python-1.onrender.com)

---

## 📘 Overview
This project develops an interactive **dashboard using Dash** to analyze supermarket sales data.  
It was built as part of a **Python-Dash course (Master 1 ECAP, 2024–2025)**, under the supervision of **M. Abdoul Razac SANE**.

**Objectives**
- Provide a visual and interactive analysis of supermarket sales.  
- Allow filtering by **gender** and **city**.  
- Display dynamic **indicators** and **graphs** for decision support.

---

## ⚙️ Features
- Total purchase amount indicator (sum of total sales).  
- Total number of purchases indicator (unique invoices).  
- Interactive histogram of total purchase amounts by gender and city.  
- Pie chart showing the distribution of product categories.  
- Line chart tracking the weekly evolution of total purchases by city.  
- French-translated data columns and user interface.  
- Real-time interaction through Dash callbacks.  

---

## 🧰 Tech Stack
**Language:** Python  
**Libraries:** pandas, Dash, dash-bootstrap-components, plotly.express, plotly.graph_objects  

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/supermarket-sales-dashboard.git
cd supermarket-sales-dashboard
pip install -r requirements.txt
```

> À compléter – specify dependencies in `requirements.txt`.

---

## 📚 Usage Example

```python
python app.py
```

Then open your browser at [http://localhost:8000](http://localhost:8000).

> The application will launch the dashboard interface with filters for gender and city, displaying indicators and graphs accordingly.

---

## 📂 Project Structure

```
supermarket-sales-dashboard/
│
├── supermarket_sales_dashboard/
│   └── supermarket_sales.csv       # Dataset
├── app.py                          # Main Dash application
├── requirements.txt
└── README.md
```

---

## 📊 Results
The dashboard displays:
- Total purchase amount and number of purchases.
- Histogram of total purchases by gender and city.
- Pie chart of product category distribution.
- Line chart of weekly sales evolution by city.

> À compléter – include a screenshot of the dashboard (e.g., `assets/dashboard_preview.png`).

---

## 🧠 References
Dataset source: `supermarket_sales.csv`  
Assignment reference: *Python-Dash Course – Master 1 ECAP (2024–2025)*

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
Developed under the guidance of **M. Abdoul Razac SANE**.  
Special thanks to the open-source Dash and Plotly communities for their documentation and tools.
