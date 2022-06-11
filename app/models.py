from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Profile model is contained inside the users application


class Project(models.Model):
    projectName = models.CharField(max_length=30)
    projectImage = CloudinaryField('image')
    projectLink = models.URLField
    projectDescription = models.TextField
    projectCategory = models.CharField(max_length=60)
    projectTechnology = models.CharField(max_length=60)
    projectOwner= models.ForeignKey(User, on_delete=models.CASCADE)
    uploadDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.projectName


# Find out whether I need to add tags