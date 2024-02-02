
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
  path('',projecthomepage,name="adminhomepage"),
  path('signup/',signup,name='signup'),
  path('signup1/', signup1, name='signup1'),
  path('login/',login,name='login'),
  path('login1/',login1,name='login1'),
  path('logout/',logout,name='logout'),

]



