from utils.preprocess import preprocess_input
from utils.email_alert import send_fraud_alert
#

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/fraud_detection.pkl")

# Title and description
st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and click the Predict button.")
st.divider()

# Input fields
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)  # ✅ fixed typo here
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,  # ✅ correct column name
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")
    if prediction == 1:
        st.error("⚠️ This transaction can be fraud")
    else:
        st.success("✅ This transaction looks like it is not a fraud")


        
# import sys
# import os
# import streamlit as st
# import pandas as pd
# import joblib

# # Add parent directory to path for module imports
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # Import custom utilities
# from utils.preprocess import preprocess_input
# from utils.email_alert import send_fraud_alert

# # Load model
# model_path = os.path.join("models", "fraud_detection.pkl")
# model = joblib.load(model_path)

# # App UI
# st.set_page_config(page_title="Fraud Detection App", page_icon="🔍")
# st.title("🔍 Fraud Detection Prediction App")
# st.markdown("Enter transaction details below and click **Predict** to check for fraud.")
# st.divider()

# # Input Fields
# transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
# amount = st.number_input("Amount", min_value=0.0, value=1000.0)
# oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)
# newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
# oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
# newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# # Prediction logic
# if st.button("Predict"):
#     try:
#         # Prepare input
#         input_data = pd.DataFrame([{
#             "type": transaction_type,
#             "amount": amount,
#             "oldbalanceOrg": oldbalanceOrg,
#             "newbalanceOrig": newbalanceOrig,
#             "oldbalanceDest": oldbalanceDest,
#             "newbalanceDest": newbalanceDest
#         }])

#         # Preprocess input
#         preprocessed_data = preprocess_input(input_data)

#         # Prediction
#         prediction = model.predict(preprocessed_data)[0]

#         # Display result
#         st.subheader(f"Prediction: `{int(prediction)}`")

#         if prediction == 1:
#             st.error("⚠️ This transaction **may be fraudulent**.")
#             send_fraud_alert(input_data)
#             st.info("🚨 Alert sent to the fraud investigation team.")
#         else:
#             st.success("✅ This transaction appears **non-fraudulent**.")
#     except Exception as e:
#         st.error(f"🚫 An error occurred during prediction: {e}")
