import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#email config
sender_email = ""
reciever_email= ""
password = ""

#creae the email content
subject = "Test Email"
body = "Hello, this is a test email"

message = MIMEMultipart()
message["From"]= sender_email
message["To"]= reciever_email
message["Subject"]= subject

message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()#upgrade the cinnection to secure and encrypted ssl/tsl connections
    server.login(sender_email, password) #login to your email account
    server.send_message(message) #send the email
    
print("Email has been sent :)")
