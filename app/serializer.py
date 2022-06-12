from asyncore import read
from xml.parsers.expat import model
from . models import Profile, Post
from rest_framework import serializers
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['id', 'name', 'profile_photo', 'bio', 'location', 'contact']
        

class PostSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'description', 'technologies', 'image', 'user', 'date']


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="app:user-detail")
    profile = ProfileSerializer(read_only=True)
    posts = PostSerializer(read_only=True,many=True)
    
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'profile', 'posts']
