# 🌿 Week 3 – Smart Irrigation System (Streamlit UI)

In Week 3, the Smart Irrigation System was enhanced by building an **interactive web application** using **Streamlit**. This app allows users to simulate real-time irrigation decisions by entering **scaled sensor values**. Based on these inputs, the app uses the trained machine learning model to predict the ON/OFF status of each sprinkler (parcel_0, parcel_1, parcel_2).

---

## 📌 Highlights

- ✅ Deployed the machine learning model via a **web-based UI**
- ✅ Used **20 sliders** to represent scaled environmental sensor inputs (0.0 to 1.0)
- ✅ Displayed sprinkler status predictions with clear ON/OFF feedback
- ✅ Enabled real-time inference using the trained `.pkl` model from Week 2

---

## 🖼️ Application Overview

### UI Features:
- **Title & Subheader** for a clean interface
- **20 sliders** for sensor input simulation
- **Prediction button** for real-time model inference
- **Results section** showing which sprinklers are ON/OFF

### 🔍 Prediction Output:
```

🔹 Sprinkler 0 (parcel_0): ON ✅
🔹 Sprinkler 1 (parcel_1): OFF ❌
🔹 Sprinkler 2 (parcel_2): ON ✅

````

---

## 🗂️ Files

| File Name                   | Description                                      |
|----------------------------|--------------------------------------------------|
| `app.py`                   | Main Streamlit app code                          |
| `Farm_Irrigation_System.pkl` | Trained ML model from Week 2                    |
| `scaler.pkl`               | Scaler used to normalize input features          |

---

## 🚀 How to Run Locally

### ✅ Step 1: Install dependencies
```bash
pip install streamlit joblib numpy
````

### ✅ Step 2: Run the app

```bash
streamlit run app.py
```

> Make sure `Farm_Irrigation_System.pkl` and `scaler.pkl` are in the same directory.

---

## 🔧 Tech Stack

* **Streamlit** – for building the UI
* **Joblib** – for loading the pre-trained model
* **NumPy** – for handling input data
* **RandomForestClassifier (Scikit-learn)** – model trained in Week 2

---