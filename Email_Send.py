from email.message import EmailMessage
from Python_App_PW_Gmail import password
import ssl
import smtplib
email_sender='wangluyufl@gmail.com'
email_password=password
email_receiver='wangluyufl@yahoo.com'
subject="You are hacked by python"
body="""
Surprise: you got the email from my python file Blar Blar Blar

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())