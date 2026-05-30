import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#load dotenv file
import os
from dotenv import load_dotenv

#load dotenv file
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSKEY = os.getenv("SENDER_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def singleEmaiSender(to_email:str, subject:str,body:str):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    print(SENDER_EMAIL)
    print(SENDER_PASSKEY)
    server = None
    try:
        # creating SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # start server
        server.starttls()
        #loginto server
        server.login(SENDER_EMAIL, SENDER_PASSKEY)
        #send Email
        server.sendmail(from_addr=SENDER_EMAIL,
                        to_addrs=to_email,
                        msg=msg.as_string())
        print(f"Email send Sucessfully to {to_email}")
    except Exception as e:
        print(f"Unable to send email {to_email}")
        print(f"Reason: {e}")
    finally:
        #close server
        if server is not None:
            server.quit()

to_email = input("Enter Reciever Email Address:")
subject = input("Enter the subject:")
body = input("Enter Email body:")
#call single email sender function
singleEmaiSender(to_email=to_email,subject=subject,body=body)