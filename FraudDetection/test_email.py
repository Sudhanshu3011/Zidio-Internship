# test_email.py

from utils.email_alert import send_fraud_alert

send_fraud_alert({
    "transaction_id": "TXN12345",
    "amount": 1000,
    "location": "Mumbai",
    "status": "Fraud Detected"
})
