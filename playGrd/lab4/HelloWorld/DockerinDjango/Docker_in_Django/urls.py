from django.urls import path
from Docker_in_Django import views

urlpatterns = [
    path('', views.Docker_in_Django, name='Docker_in_Django'),
]