from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_registration_email


User = get_user_model()

@receiver(post_save, sender=User)
def send_mail_user(sender, instance,created,**kwargs):
    if created:
        send_registration_email.delay(instance.id)