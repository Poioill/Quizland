from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('', Categories.as_view(), name='category'),
    path('categories/<int:pk>/', SubjectsDetailView.as_view(), name='subjects'),
    path('materials/', MaterialsTemplateView.as_view(), name='materials'),
    path('materials/', SubjectMaterialListView.as_view(), name='subjectmaterial'),
    path('privacy/', PrivacyTemplateView.as_view(), name='privacy'),
    #path('categories/<int:pk>/', Area.as_view(), name='subject_areas'),
    #path('materials/<int:pk>/', SubjectMaterialView.as_view(), name='subjects'),
]