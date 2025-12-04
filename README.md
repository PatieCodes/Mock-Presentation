# Mock-Presentation


This project demonstrates how to build a simple, modular dashboard using Streamlit. The structure is easy to follow, making it great for beginners learning how to organize a Streamlit app.

---

## 📁 Project Structure

```
project/
│
├── charts/              # Stores chart-related helper scripts (optional)
├── data/                # Contains datasets used by the dashboard
│
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd project
```

### 2. Install dependencies

Make sure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run main.py
```

---

## 📊 What This App Does

* Loads data from the **data** folder
* Generates charts or visual elements located in the **charts** folder
* Displays everything on an interactive Streamlit dashboard

---

## 🛠 Requirements

All required Python packages are listed in `requirements.txt`.

---

## ✨ Notes

* Keep datasets small for faster loading.
* You can add more charts by placing scripts inside the `charts` folder and importing them into `main.py`.


