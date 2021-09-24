from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import message, send_mail
# from uuid import uuid4 as uuid

from django.conf import settings


class User(AbstractUser):

    username = None
    email = models.CharField(max_length=128, unique=True,db_index=True)
    mobile = models.CharField(max_length=14,db_index=True)
    # is_email_verified = models.BooleanField(default = False)
    # is_phone_verified = models.BooleanField(default = False)
    # otp = models.CharField(max_length =6,null = True, blank = True)
    # email_verification_token = models.CharField(max_length=100, null=True, blank=True)
    # forget_password = models.CharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    objects = UserManager()

    # def name(self):
    #     return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email

# @receiver(post_save, sender = User)
# def send_email_token(sender, instance, created, **kwargs):
#     try:
#        subject = 'Youe email needs to be verified'
#        message = f'Hi, click on the link to verify email {uuid()}'
#        email_from = settings.EMAIL_HOST_USER
#        recipient_list = [instance.email]
#        send_mail(subject, message, email_from, recipient_list)
#     except :
#         pass
