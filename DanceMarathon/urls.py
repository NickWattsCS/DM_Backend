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
from users import users.views

router = routers.SimpleRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet)
router.register(r'dancers', DancerViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'groups', GroupsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('events/', EventViewSet),
    path('users/', include('users.urls')),
    path('users/dancers', users.views.DancerViewSet),
    path('users/staff', users.views.StaffViewSet),
    path('users/guests', users.views.GuestViewSet),
    path('groups/', GroupsViewSet),
]
