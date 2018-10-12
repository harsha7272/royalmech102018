import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("harsharam76@gmail.com", "*****************") 
  
# message to be sent 
message = "message"
  
# sending the mail 
s.sendmail("harsharam76@gmail.com", "anilbiju8@gmail.com", message) 

print("sent")

# terminating the session 
s.quit() 