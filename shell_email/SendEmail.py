
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
s = smtplib.SMTP_SSL('smtp.gmail.com', 465) # creates SMTP session 
s.login("shuksgal13@gmail.com", "shuksratsiv13") # Authentication 
MailFrom = "shuksgal13@gmail.com"
MailTo = "shuksgal13@com"
message = 'Subject: {}\n\n{}'.format("Hello World", "Hello World test email")
#message = 'Subject: {}\n\n{}'.format("SpamTest", "Hello world! Test Email")
s.sendmail(MailFrom,MailTo, message) # sending the mail 
s.quit() # terminating the session 

