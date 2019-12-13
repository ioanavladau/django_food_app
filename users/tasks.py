from celery import task
# from django.core.mail import send_mail
from .models import Profile
import smtplib


@task
def profile_created():
    gmail_user = '' #TO ADD: email
    gmail_password = '' #TO ADD: pwd

    sent_from = gmail_user
    to = ['', ''] #TO ADD: email addresses to send the email to

    subject = "Hi Henrik! :)"
    text = "This message was sent with Python's smtplib."
    
    message = 'Subject: {}\n\n{}'.format(subject, text)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

# def profile_created(profile_id):
#     profile = Profile.objects.get(id=profile_id)
#     # profileEmail = Order.objects.get(id=profile_email)
#     # to = orderEmail
#     # gmail_user = email from
#     # gmail_pwd = pwd
#     smtpserver = smtplib.SMTP("smtp.gmail.com",587)
#     smtpserver.ehlo()
#     smtpserver.starttls()
#     smtpserver.ehlo
#     smtpserver.login(gmail_user, gmail_pwd)
#     header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: Profile created #{}'.format(profile.id)
#     print(header)
#     # message = 'Subject: {}\n\n{}'.format(subject, text)
#     subject = 'Profile Confirmation #{}'.format(order.id)
#     text = 'Dear {},\n\nYou have successfully created a profile. Your profile is #{}.'.format(order.first_name,order.id)
#     message = 'Subject: {}\n\n{}'.format(subject, text)
#     smtpserver.sendmail(gmail_user, to, message)
#     print('Done!')
#     smtpserver.close()
