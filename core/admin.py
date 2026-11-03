from django.contrib import admin
from .models import Household, Member

# Register your models here.

admin.site.register(Household)
admin.site.register(Member)