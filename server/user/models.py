from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES_CHOICES = (
        ('employer', 'Employer'),
        ('employee', 'Employee')
    )

    first_name = models.CharField('first_name', max_length=150)
    last_name = models.CharField('last_name', max_length=150)
    email = models.EmailField('email', unique=True)
    role = models.CharField('role', max_length=10, choices=ROLES_CHOICES)

    class Meta:
        db_table = 'users'
