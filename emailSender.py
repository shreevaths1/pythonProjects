from email.message import EmailMessage
import ssl
import smtplib

email_sender = ""
email_password = ""

email_reciever = ""

subject = "Don't forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

# creating an EmailMessage instance
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["subject"] = subject
em.set_content(body)

# creating SSL Context Object (Secure Sockets Layer)
# SSLContext acts as a placeholder where the policies
# and artifacts related to the secure communication of
# a client or a server can be stored. Creation of an SSLContext instance
# is generally the first step required in any SSL based server or client.

context = ssl.create_default_context()

# Secure Mail transfer Protocol
# SMTP (Simple Mail Transfer Protocol) is a TCP/IP protocol used in
# sending and receiving email. SMTP is used most commonly by email clients,
# including Gmail, Outlook, Apple Mail and Yahoo Mail.

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
