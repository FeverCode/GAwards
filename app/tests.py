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

class TestPost(TestCase):
    def test_post(self):
        self.assertEqual(1, 1)
    
    def setUp(self):
        self.user = User.objects.create_user(id=1,username='testuser', password='12345')
        self.user.save()
        self.post = Post.objects.create(id=1,user=self.user,title='test title')
        self.post.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))
        
        
    def test_save(self):
        self.post.save()
        post= Post.objects.all()
        self.assertTrue(len(post) > 0)
        
    def test_delete(self):
        self.post.delete()
        post = Post.objects.all()
        self.assertTrue(len(post) == 0)
        
    def test_search_projects(self):
        self.post.save()
        post = Post.search_projects('test')
        self.assertTrue(len(post) > 0)
        
    def test_all_posts(self):
        self.post.save()
        post = Post.all_posts()
        self.assertTrue(len(post) > 0)
        
    def get_post(self):
        self.post.save()
        post = Post.get_post(1)
        self.assertTrue(len(post) > 0)
        
    # def test_get_ratings(self):
    #     self.post.save()
    #     post = Post.get_ratings(1)
    #     self.assertTrue(len(post) > 0)
        
        