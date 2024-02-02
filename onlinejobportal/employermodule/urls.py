
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
  path('',projecthomepage,name="employerhomepage"),
  path('jobpost',jobpost,name="jobpost"),
  path('add_job',add_job_details,name="add_job_details"),
  path('view/',view_job_details,name="view_job_details"),
  path('edit/<int:pk>',edit, name="edit"),
  path('remove/<int:pk>',remove, name='remove'),
  path('job_application_list/',job_application_list,name="job_application_list"),





]
