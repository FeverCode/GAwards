from django.test import TestCase
from .models import *

# Create your tests here.

class TestApp(TestCase):
    def test_app(self):
        self.assertEqual(1, 1)

class TestProject(TestCase):
    def test_project(self):
        self.assertEqual(1, 1)


class TestProfile(TestCase):
    def test_profile(self):
        self.assertEqual(1, 1)
    
    def setUp(self):
        self.user = User.objects.create_user(id=1,username='testuser', password='12345')
        self.user.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        
    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
        
    def test_delete(self):
        self.user.delete()
        users = User.objects.all()
        self.assertTrue(len(users) == 0)


        
   