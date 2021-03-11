import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver,content):
    email="michael.wings.red@outlook.com"
    password="mchl2004"
    smtp=smtplib.SMTP('smtp.office365.com',587)
    smtp.starttls()
    smtp.login(email,password)
    message=MIMEMultipart()
    message["From"]=email
    message["To"]=receiver
    message["Subject"]="Email Confirmation"
    message.attach(MIMEText(content,"html"))
    smtp.send_message(message)
    smtp.quit()