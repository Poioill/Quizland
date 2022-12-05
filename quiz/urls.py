from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('', Categories.as_view(), name='category'),
    path('categories/<int:pk>/', SubjectsDetailView.as_view(), name='subjects'),
]