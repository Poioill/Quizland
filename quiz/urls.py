from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index),
    path('about-uni/', About_Uni.as_view()),
]
