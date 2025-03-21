from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_registration_email(user_id):
    user = User.objects.get(id=user_id)
    subject = 'Welcome to our price comparison website'
    msg = f'Hi {user.username}, Welcome to our website happy to have you'
    send_mail(subject,msg,settings.EMAIL_HOST_USER, [user.email])