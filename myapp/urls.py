from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:file_id>/download/', views.download_file, name='download_file'),
    path('files/<int:file_id>/open/', views.open_file, name='open_file'),
]
