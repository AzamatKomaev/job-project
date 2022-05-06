from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES_CHOICES = (
        ('employer', 'Employer'),
        ('employee', 'Employee')
    )

    first_name = models.CharField('first_name', max_length=150)
    last_name = models.CharField('last_name', max_length=150)
    role = models.CharField('role', max_length=10, choices=ROLES_CHOICES)
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with such an email is already exists'
        }
    )

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
