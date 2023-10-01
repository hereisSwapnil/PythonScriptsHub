import os 

print("1. Shutdown")
print("2. Reboot")
print("3. Lock")
print("4. Sign Out")
user_input = int(input("Please provide your input [1/2/3/4]: "))  


def shutdown():
    os.system("shutdown /s /t 1") 

def reboot():
    os.system("shutdown /r /t 1")

def logoff():
    os.system("shutdown /l")

def lockpc():
    os.system(r'"C:\Windows\System32\rundll32.exe user32.dll,LockWorkStation"')

if user_input == 1:
    shutdown()
elif user_input == 2:
    reboot()
elif user_input == 3:
    lockpc()
elif user_input == 4:
    logoff()
else:
    exit()