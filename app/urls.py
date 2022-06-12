from django.urls import include, path
from app import views
from rest_framework.routers import DefaultRouter
from .views import RegisterView
from django.contrib.auth import views as auth_views
from .views import *
from .forms import LoginForm
from django.conf.urls import url



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet,  basename="posts")
router.register('profile', views.ProfileViewSet, basename="profile")


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('user/profile/', views.user_profile, name='user-profile'),
    path('profile/', views.profile, name='profile'),
    
    
]