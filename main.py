from info import *
from email.message import EmailMessage
import ssl
import smtplib

# Account info 
email_sender = email_sender
email_pass = email_pass

# Email Info 
email_recever = ['giyaxor112@laluxy.com','samircd4@gmail.com']
email_sub = 'Test mail'
email_body = """
Hey guys, please like my code and share
I'm a Python startup programer
"""
# Make an instance
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_recever
em['subject'] = email_sub
em.set_content(email_body)

context = ssl.create_default_context()
# Final step 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_recever, em.as_string())

# Thank you