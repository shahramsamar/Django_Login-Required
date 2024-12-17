
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        permissions = [
            ('view_login', 'Can view login page'),
        ]

    def __str__(self):
        return self.username
