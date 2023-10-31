import smtplib
from email.message import EmailMessage
from string import Template

email = EmailMessage()
email['from'] = 'Shital Moule'
email['to'] = 'shitalmoule1234@gmail.com'
email['subject'] = 'You Won The Dollars!'

email.set_content('I am learning Python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shitalmoule17@gmail.com', 'shital@1234')
    smtp.login()
    smtp.send_message(email)
    print("Email Sent!!")