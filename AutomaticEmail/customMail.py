import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "sender@email.com"
receiver_email = "receipient@email.com"
password = "App_password"  # App Password if using 2FA
subject = "Custom Subject"
message = "Hello, this is a custom email message!"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
 
# Authentication
s.login(sender_email, password)
 
# message to be sent
text = msg.as_string()

# sending the mail
s.sendmail(sender_email, receiver_email, text)
 
# terminating the session
s.quit()

print("email sent successfully")