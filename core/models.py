from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Household(models.Model):

    name = models.CharField(max_length=100)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    invite_code = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Member(models.Model):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    household = models.ForeignKey(Household, on_delete=models.CASCADE)

    display_name = models.CharField(max_length=100)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default="member")

    avatar_colour = models.CharField(max_length=20, default="blue")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name

    