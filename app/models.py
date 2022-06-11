from django.db import models

class Project(models.Model):
    projectName = models.CharField(max_length=30)
    projectImage = models.ImageField
    projectLink = models.URLField
    projectDescription = models.TextField
    uploadDate = models.DateTimeField(auto_now_add=True)

