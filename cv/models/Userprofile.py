from django.contrib.auth.models import User
from django.db import models


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    about = models.TextField(null=True)
    experience = models.TextField(null=True)
    certificates = models.TextField(null=True)
    education = models.TextField(null=True)
    skills = models.TextField(null=True)
    accomplishments = models.TextField(null=True)
    interesting_positions = models.TextField(null=True)
    # picture = models.ImageField(upload_to='static/profile_pictures', blank=True, null=True)
    # authentication_key = models.CharField(max_length=50)
    session_key = models.CharField(null=True, blank=True, max_length=160)
    authentication_key = models.CharField(null=True, blank=True, max_length=50)
