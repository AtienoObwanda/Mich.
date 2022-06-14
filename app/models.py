from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Profile model is contained inside the users application


class Project(models.Model):
    projectName = models.CharField(max_length=30)
    projectImage = CloudinaryField('image')
    # projectImage = models.ImageField(upload_to='projectPics')
    projectLink = models.URLField(max_length=200, null=True, blank=True)
    projectDescription = models.TextField(max_length=500, blank=True, default=f'Project Description')
    projectCategory = models.CharField(max_length=60)
    projectTechnology = models.CharField(max_length=60)
    projectOwner= models.ForeignKey(User, on_delete=models.CASCADE)
    uploadDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return str (self.projectName)

    def saveProject(self):
        self.save()

    def deleteProject(self):
        self.delete()
    
    def updateProjectName(self, new_projectName):
        self.projectName = new_projectName
        self.save()

    @classmethod
    def getProjectId(cls, project_id):
        project = Project.objects.filter(project_id=project_id).all()
        return project

    @classmethod
    def getUserProjects(cls, user_id):
        userProject = Project.objects.filter(user_id=user_id).all()
        return userProject

    @classmethod
    def getProjects(cls):
        allProjects = cls.objects.all()
        return allProjects

    @classmethod
    def searchProject(cls, search_term):
        projectResults = Project.objects.filter(sitename__icontains=search_term)
        return projectResults



class Comment(models.Model):
    comment = models.TextField()
    createDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def updateComment(self, new_comment):
        self.comment = new_comment
        self.save()
  
    def __str__(self):
        return f'Comment by: {self.author}'

    @classmethod
    def get_comments(cls,id):
            comments = cls.objects.filter(project_id=id)
            return comments     


class Review(models.Model):
    REVIEW = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design = models.IntegerField(default=0, choices=REVIEW, null=True)
    usability = models.IntegerField(default=0, choices=REVIEW, null=True)
    content = models.IntegerField(default=0, choices=REVIEW, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()
