
# 🌱 Week 2 – Smart Irrigation System

This week focuses on building a complete machine learning pipeline for **automated irrigation control** using environmental sensor data. We scale the features, train a multi-label classification model, visualize irrigation patterns, and save the trained model for deployment.

---

## 📁 Files Included

- `Irrigation_System.ipynb` – Main notebook containing all Week 1 + Week 2 code
- `irrigation_machine.csv` – Dataset used for training and visualization
- `Farm_Irrigation_System.pkl` – Trained irrigation prediction model
- `scaler.pkl` – Feature scaler for future predictions

---

## ⚙️ Key Steps

### ✅ 1. Feature Scaling

Used `MinMaxScaler` to normalize 20 sensor readings into a 0–1 range for consistent model performance.

```python
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
````

---

### ✅ 2. Train-Test Split

Split the dataset into 80% training and 20% testing for model evaluation.

```python
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

---

### ✅ 3. Model Training

Trained a `MultiOutputClassifier` using a tuned `RandomForestClassifier` to predict irrigation requirements (`parcel_0`, `parcel_1`, `parcel_2`).

```python
rf = RandomForestClassifier(n_estimators=200, max_depth=10, ...)
model = MultiOutputClassifier(rf)
model.fit(X_train, y_train)
```

---

### ✅ 4. Evaluation

Generated a **classification report** to assess performance of the trained model.

```python
print(classification_report(y_test, y_pred, target_names=y.columns))
```

---

### ✅ 5. Visualization

Created visualizations for:

* Individual parcel pump status using square waves
* Combined irrigation patterns over time

```python
plt.step(df.index, df['parcel_0'], where='post', ...)
```

![](example_output.png) <!-- Optionally include sample plot here -->

---

### ✅ 6. Saving the Model

Exported the model and scaler for future predictions or deployment.

```python
joblib.dump(model, "Farm_Irrigation_System.pkl")
joblib.dump(scaler, "scaler.pkl")
```

---

## 📌 Summary

* Built a robust multi-label classifier for smart irrigation.
* Added sensor scaling, model training, performance evaluation, and insightful irrigation visualizations.
* Prepared models for use in automation pipelines.

---
