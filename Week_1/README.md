# 🚿 Smart Irrigation System – Week 1

This repository contains the initial implementation for the **Smart Irrigation** project developed as part of the AICTE internship (July 2025).

The aim is to **automate irrigation decisions** using sensor data (e.g., soil moisture, temperature, humidity) by training a machine learning model that can predict the right irrigation actions.

---

## 📁 Files Included

- `Smart_Irrigation.ipynb`: Jupyter notebook with data loading, preprocessing, feature-label setup, and EDA steps.
- `irrigation_machine.csv`: Dataset containing sensor readings and corresponding irrigation actions.

---

## 🧠 Project Overview

### 🔸 Objective
Build a model to classify multiple irrigation actions based on 20 sensor readings. These actions include turning on/off irrigation systems, water level control, etc.

### 🔸 Dataset Info
- **Rows:** ~5000+
- **Input Features:** `sensor_0` to `sensor_19`
- **Output Labels:** Multiple binary targets representing irrigation decisions
- **Source:** Provided via internship LMS

---

## 🧪 Step-by-Step Implementation

### 1. 📦 Import Libraries
Standard data science and ML libraries like:
- `pandas`, `matplotlib`, `seaborn`
- `scikit-learn` for model building and evaluation
- `joblib` for model saving

### 2. 📥 Load & Explore Dataset
```python
df = pd.read_csv("irrigation_machine.csv")
df.info()
df.describe()
````

* Dropped unnecessary column: `Unnamed: 0`

### 3. 🧹 Preprocessing

* Extracted feature matrix `X` (`sensor_0` to `sensor_19`)
* Extracted multi-label targets `y` (columns 20 onward)

### 4. 🧾 Output

* `X.shape`: Input features → (samples, 20)
* `y.shape`: Output labels → (samples, multi-targets)

---
