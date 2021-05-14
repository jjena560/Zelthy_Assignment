import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = input("Enter your mail and press enter: ")
password = input("Type your password and press enter: ")
message = input("Enter the body of the mail and press Enter:\n ")
receiver_email_id = input("Enter reciever's email id and press enter: ")

# this will secure the server
context = ssl.create_default_context()


try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() 
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    # this will send the login request
    server.login(sender_email, password)
   
    # sending the mail
    server.sendmail(sender_email, receiver_email_id, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
