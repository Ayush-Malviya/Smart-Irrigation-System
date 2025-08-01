import streamlit as st
import numpy as np
import joblib  

# Load the trained machine learning model
model = joblib.load("Farm_Irrigation_System.pkl")  

# Streamlit UI
st.set_page_config(page_title="Smart Irrigation System", layout="centered")
st.title("🌱 Smart Sprinkler Prediction System")
st.markdown("Enter the **scaled sensor values** (between 0.0 and 1.0) to get sprinkler ON/OFF predictions.")

# Collect sensor inputs via sliders
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

# Predict sprinkler activation
if st.button("🔍 Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.success("✅ Prediction Complete!")
    st.markdown("### 🚿 Sprinkler Status:")
    for i, status in enumerate(prediction):
        st.write(f"🔹 Sprinkler {i} (parcel_{i}): **{'ON ✅' if status == 1 else 'OFF ❌'}**")
