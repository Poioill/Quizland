from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('', Categories.as_view(), name='category'),
    path('categories/<int:pk>/', SubjectsDetailView.as_view(), name='subjects'),
    path('materials/', views.materialview, name='materials'),
    path('about-us/', views.about_us, name='about_us'),
    path('privacy/', views.privacy, name='privacy'),
    path('t_service/', views.terms_of_service, name='t_service'),
]