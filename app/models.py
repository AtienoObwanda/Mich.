from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):
    projectName = models.CharField(max_length=30)
    projectImage = models.ImageField
    projectLink = models.URLField
    projectDescription = models.TextField
    projectCategory = models.CharField(max_length=60)
    projectTechnology = models.CharField(max_length=60)
    projectOwner= models.ForeignKey(User, on_delete=models.CASCADE)
    uploadDate = models.DateTimeField(default=timezone.now)



# Find out whether I need to add tags