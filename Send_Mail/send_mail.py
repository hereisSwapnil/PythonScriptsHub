import smtplib

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    print("SERVER CONNECTED")
except:
    print("Could Not connect to Gmail")

user = input("Enter User id\n")
Pass_w = input("\nEnter your Password\n")
reciever_id = input("\nEnter reciever id\n")
msg = input("\nEnter message\n")
try:
    print("User Logged in")
except:
    print("Allow Less secure apps in GOOGLE ACCOUNT SETTINGS to use SMTP services")
    server.quit()
    exit()

server.sendmail(user, reciever_id, msg)
print("MAIL sent")

print("Closing Connection")
server.quit()
print("Server closed")
