import smtplib

sender = "sender@example.com"
receiver = "receiver@example.com"

message = "\r\n".join([
    "From: From Sender <sender@example.com>",
    "To: To Receiver <receiver@example.com>",
    "Subject: Mail test",
    "",
    "Hello World!",
])

try:
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.sendmail(sender, receiver, message)
    print("Message successfully sent!")
except smtplib.SMTPException:
    print("Error: unable to send email")

