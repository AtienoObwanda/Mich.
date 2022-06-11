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

