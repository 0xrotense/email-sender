# Import all required modules

from email.message import EmailMessage
from dotenv import load_dotenv
import os
import ssl
import smtplib

# This loads the environment variable

load_dotenv()

# Import those variables from .env file

email_sender = os.getenv("email")
email_password = os.getenv("password")

# Tested with a temporary email

email_receiver = 'hakele3350@laserlip.com'

subject = "I'm a python mailer, I work"
body = """
Hi, Buddy

Hope you're good engineer?
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())