import getpass
import smtplib

HOST = "smtp-mail.gmail.com"
PORT = 587
From_emai = "nithx042@gmail.com"
to_email = ""
password = getpass.getpass("Enter password:  ")
message = """Subject: Greeting from Habit Tracker
Hello ">>>>" 
This email is about your weekly progress

Thanks,"""
smtp = smtplib.SMTP(HOST, PORT)
status_code ,response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")
status_code ,response = smtp.starttls()
print(f"[*] Starting TLS connection : {status_code} {response}")
status_code ,response = smtp.login(From_emai , password)
print(f"[*] Logging in : {status_code} {response}")
smtp.sendmail(From_emai,to_email,message)
smtp.quit()