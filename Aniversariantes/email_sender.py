import ssl
import smtplib
from email.message import EmailMessage
import streamlit as st


class GmailSender:
    def __init__(self):
        self.email_address = st.secrets['EMAIL_ADDRESS']
        self.email_password = st.secrets['EMAIL_PASSWORD']

    def send_email(self, to: str, subject: str, body: str):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.email_address
        msg["To"] = to
        msg.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(self.email_address, self.email_password)
            smtp.send_message(msg)



