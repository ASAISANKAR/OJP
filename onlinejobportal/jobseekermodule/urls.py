
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
  path('',projecthomepage,name="jobseekerhomepage"),
  path('viewjobs',viewjobs,name="viewjobs"),
  path('job_details_list', job_details_list, name="job_details_list"),
  path('submit_form/',submit_form,name='submit_form'),
  path('addjobseekerprofile/',addjobseekerprofile,name='addjobseekerprofile'),
  path('apply_to_job/<int:job_id>',apply_to_job,name='apply_to_job'),


]
