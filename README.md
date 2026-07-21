# AI Customer Intelligence Platform V2 Pro

A production-ready AI-powered Customer Intelligence Platform built with Streamlit.

## Features

- AI Customer Segmentation
- KMeans Clustering
- StandardScaler Pipeline
- Customer Health Score
- Churn Risk Prediction
- Loyalty Level Analysis
- Executive Summary Dashboard
- Customer Search
- CSV Upload
- Excel Upload
- CSV Download
- Excel Download
- Plotly Interactive Dashboard
- Glassmorphism UI

---

## Installation

Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Generate sample data

```bash
python generate_data.py
```

Run

```bash
streamlit run app.py
```

---

## Project Structure

```
AI_Customer_Intelligence_V2_Pro
│
├── app.py
├── ai_engine.py
├── dashboard.py
├── customer_search.py
├── executive_summary.py
├── upload_data.py
├── report_generator.py
├── generate_data.py
├── utils.py
├── theme.py
│
├── assets
│   └── style.css
│
├── data
│   └── customer_data.csv
│
└── reports
```

---

Built using

- Streamlit
- Plotly
- Pandas
- NumPy
- Scikit-Learn
- Faker