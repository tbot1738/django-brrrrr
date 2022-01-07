from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('post', Home_Page),
    path('upload', ImageUploader),
]

