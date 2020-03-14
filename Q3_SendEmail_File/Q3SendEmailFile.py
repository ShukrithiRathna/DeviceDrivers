'''
    Shukrithi Rathna
    CED16I031
    23/2/20
    Program to send email if file is larger than 100 bytes.

    This program scans all the .txt files in the current direrctory 
    and sends an email if file is larger than  100 bytes.

    Email authentication and set  up required if email details are changed
'''


import smtplib 
def SendEmail(FileName):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465) # creates SMTP session 
    s.login("bcd@gmail.com", "******") # Authentication Enter email id and password of receiver
    message = "Subject: {}\n\n This is to inform you that a large file of size > 100 bytes was found: {}".format("Large File Found",FileName)
    s.sendmail("bcd@gmail.com ", "ced16i031@iiitdm.ac.in", message) # sending the mail
    s.quit() # terminating the session 

import os 

#print(os.scandir())
files = [f for f in os.listdir('.') if f.endswith(".txt")]
for f in files:
    fsize=os.path.getsize(f)
    print("File:",f," Size: ",fsize)
    if fsize>100:
        SendEmail(f)
