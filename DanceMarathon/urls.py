"""DanceMarathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events.views import EventViewSet
from users.views import DanceUserViewSet, CustomAuthToken
from groups.views import GroupViewSet
from teams.views import TeamViewSet
from rest_framework.authtoken.views import obtain_auth_token
import groups.urls
import users.urls

jimmy = routers.DefaultRouter()
jimmy.register(r'events', EventViewSet)
jimmy.register(r'users', DanceUserViewSet)
jimmy.register(r'groups', GroupViewSet)
jimmy.register(r'teams', TeamViewSet)

urlpatterns = [
    path("", include(jimmy.urls)),
    path('func/groups/', include(groups.urls)),
    path('func/users/', include(users.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
