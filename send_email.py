import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver,content,subject):
    email="michael.wings.red@outlook.com"
    password="mchl2004"
    smtp=smtplib.SMTP('smtp.office365.com',587)
    smtp.starttls()
    smtp.login(email,password)
    message=MIMEMultipart()
    message["From"]=email
    message["To"]=receiver
    message["Subject"]=subject
    message.attach(MIMEText(content,"html"))
    smtp.send_message(message)
    smtp.quit()

def send_activation_mail(receiver,user):
    content="""
        <h1>Wordlib</h1>
        <a href='http://wordlib-env.eba-tbhgfmvg.us-east-1.elasticbeanstalk.com/activate/"""+str(user.id)+"""'>Click Here To Activate</a>
    """
    send_email(receiver,content,"Email Confirmation")