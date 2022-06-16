from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User

from .models import *


# Tests for the user profile are in the users application



class ProjectTest(TestCase):
    def setUp(self):
        self.test_user = User(username='Atieno', password='test123')
        self.test_user.save()

        self.test_project = Project(projectName ='Test Project Title', projectImage='demo.png',projectLink='www.example.com',projectDescription='Test project description',projectCategory = '', projectTechnology = '',projectOwner=self.test_user,uploadDate = datetime.now())


    def test_instance(self):
        self.assertTrue(isinstance(self.test_project, Project))

    def test_saveProject(self):
        self.test_project.saveProject()
        self.assertEqual(len(Project.objects.all()),1)

  

    def test_updateProjectName(self):
        self.test_project.updateProjectName( new_projectName='Updated Project Name')
        self.test_project.saveProject()

    def test_getProjectId(self):
        test_id = 1
        getProject = Project.objects.filter(id=test_id)
        self.assertEqual(len(getProject),0)

    def tearDown(self):
        self.test_user.delete()
        Project.objects.all().delete()

class ReviewTest(TestCase):
    def setUp(self):
        self.test_user = User(username='Atieno', password='test123')
        self.test_user.save()

        self.test_project = Project(projectName ='Test Project Title', projectImage='demo.png',projectLink='www.example.com',projectDescription='Test project description',projectCategory = '', projectTechnology = '',projectOwner=self.test_user,uploadDate = datetime.now())
        self.test_project.save()
        self.test_review = Review(project=self.test_project, user = self.test_user, design=6, usability=5, content=5, comment='Awesome UI')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_review, Review))

    def test_saveReview(self):
        self.test_review.saveReview()
        self.assertEqual(len(Review.objects.all()),1)

  
    def test_getReviewId(self):
        test_id = 1
        getReview = Review.objects.filter(id=test_id)
        self.assertEqual(len(getReview),0)

    def tearDown(self):
        self.test_user.delete()
        Review.objects.all().delete()


