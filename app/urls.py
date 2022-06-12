from django.urls import include, path
from app import views
from rest_framework.routers import DefaultRouter



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet,  basename="posts")
router.register('profile', views.ProfileViewSet, basename="profile")


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    
]