from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    profileImage = models.ImageField(default='default.png',upload_to='projectPics')
    bio=models.TextField(max_length=500, blank=True, default=f'Inspired to Code...')
    