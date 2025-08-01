# 💧 Smart Irrigation System using Machine Learning

This project is part of the AICTE Internship (July 2025) and focuses on building a **Smart Irrigation System** that automates sprinkler control based on environmental sensor data. The system uses **machine learning** to predict which farm parcels (sprinklers) need to be activated, based on inputs from 20 soil and weather sensors.

---

## 📌 Project Timeline & Structure

| Week | Focus                         | Key Components |
|------|-------------------------------|----------------|
| **Week 1** | Data Exploration & Preprocessing | Cleaning, feature selection, label separation |
| **Week 2** | Model Building & Evaluation | Scaling, multi-label classification, visualization |
| **Week 3** | UI Development | Streamlit web app for real-time predictions |

---

## 🧠 Problem Statement

To **automate irrigation** using smart sensors that monitor environmental conditions. The system takes **20 sensor values (scaled between 0 and 1)** as input and predicts the ON/OFF status for 3 sprinkler zones: `parcel_0`, `parcel_1`, and `parcel_2`.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Scikit-learn** – for model training and evaluation
- **Streamlit** – for building the web UI
- **Joblib** – for saving and loading the trained model

---

## 🗂️ Folder Structure

```

Smart-Irrigation-System/
│
├── irrigation_machine.csv             # Dataset
├── Irrigation_System.ipynb            # Full notebook (Week 1 & 2)
├── app.py                             # Streamlit app (Week 3)
├── Farm_Irrigation_System.pkl         # Trained model
├── scaler.pkl                         # MinMaxScaler for input normalization
├── README.md                          # Project documentation

````

---

## 🔍 How It Works

1. **Data Preprocessing**
   - Removed unnecessary columns
   - Separated 20 input features and 3 output labels
   - Scaled features using `MinMaxScaler`

2. **Model Training**
   - Used `RandomForestClassifier` wrapped in `MultiOutputClassifier` for multi-label prediction
   - Trained on 80% of data, evaluated on 20%

3. **Evaluation**
   - Used `classification_report` for precision, recall, and F1-score
   - Visualized sprinkler activation patterns across time

4. **Web UI (Streamlit)**
   - Accepts 20 scaled inputs via sliders
   - Displays real-time sprinkler ON/OFF predictions
   - Loads model from `.pkl` file

---

## ▶️ Running the App Locally

### 1. Install Required Libraries

```bash
pip install streamlit scikit-learn joblib numpy pandas matplotlib seaborn
````

### 2. Run the Streamlit App

```bash
streamlit run app.py
```

> Make sure `Farm_Irrigation_System.pkl` and `scaler.pkl` are in the same directory.

---

## 📊 Sample Prediction Output

```
🔹 Sprinkler 0 (parcel_0): ON ✅
🔹 Sprinkler 1 (parcel_1): OFF ❌
🔹 Sprinkler 2 (parcel_2): ON ✅
```

---

## 🎯 Conclusion

This Smart Irrigation System demonstrates how machine learning and interactive web apps can optimize agricultural operations by enabling data-driven, automated irrigation based on real-time environmental conditions.

---

## 📧 Author

**Ayush Malviya**   
B.Tech – Computer Science (AI & ML)     
AICTE Smart Intern, July 2025
