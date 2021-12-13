import smtplib
from email.message import EmailMessage
import schedule
import time
import sys

print('Welcome to Reminders!\n')
email = input('Enter your gmail: ')
password1 = input('Enter password: ')
subject = input('Enter the subject: ')
reminder = input('Enter the reminder: ')
email_recipient = input('Enter email recipient: ')
when = input('Enter time of reminder in HH:MM military time: ')

def email_func(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = email
    msg['from'] = user
    password = password1

    # server parameters
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

    def do_this():
        email_func(subject, reminder, email_recipient)
        sys.exit()

    # conditions for reminder
    schedule.every(1).day.at(when).do(do_this)


email_func(subject, reminder, email_recipient)


while True:
    schedule.run_pending()
    time.sleep(1)



