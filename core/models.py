from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class household(models.Model):

    name = models.CharField(max_length=100)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    invite_code = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
