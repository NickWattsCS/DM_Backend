from rest_framework.urlpatterns import format_suffix_patterns
from .views import export_DanceGroups_csv
from django.urls import path

urlpatterns = [
	path('csv-export/', export_DanceGroups_csv),
]

urlpatterns += format_suffix_patterns(urlpatterns)
