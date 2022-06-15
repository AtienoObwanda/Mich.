from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    profileImage = models.ImageField(default='default.png',upload_to='projectPics')
    bio=models.TextField(max_length=500, blank=True, default=f'Inspired to Code...')


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        
        instance.profile.save()


    def __str__(self):
        return f'{self.user.username}profile'


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, new_bio):
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        user = User.objects.get(id=user_id)
        self.photo = new_image
        self.save()

    @classmethod
    def searchProject(cls, search_term):
        profileResults = Profile.objects.filter(sitename__icontains=search_term)
        return profileResults
    

    '''

    Django signals for the Profile model are stored in the signal.py
    
    '''