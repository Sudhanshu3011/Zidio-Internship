# utils/email_alert.py

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_fraud_alert(transaction_info, recipient_email="kumarshekhar98.99@gmail.com"):
    """
    Sends an email alert when a fraudulent transaction is detected.
    
    Args:
        transaction_info (dict): Information about the transaction flagged as fraud.
        recipient_email (str): Email address to notify (default set).
    """
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    
    subject = "🚨 Fraudulent Transaction Alert"
    body = f"A transaction has been flagged as FRAUDULENT:\n\n{transaction_info}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("🚀 Alert email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)
