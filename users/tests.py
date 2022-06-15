from django.test import TestCase
from .models import Profile
from datetime import datetime
from django.contrib.auth.models import User


'''
Tests specifically for the Profile model
'''

class ProfileTest(TestCase):
    '''
    Profile model
    '''
    def setUp(self):
        self.user = User.objects.create(username='mishM')

    def tearDown(self):
        self.user.delete()

    def test_new_profile(self):
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)