from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import export_DanceUsers_csv

urlpatterns = [
	path('csv-export/', export_DanceUsers_csv),
]

urlpatterns = format_suffix_patterns(urlpatterns)
