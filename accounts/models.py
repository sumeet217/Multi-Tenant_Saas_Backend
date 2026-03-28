from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Add any additional fields you need for your user model
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
        ('MANAGER', 'Manager'),
        ('VIEWER', 'Viewer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')

    def __str__(self):
        return f'{self.username} ({self.role})'
