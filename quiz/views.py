from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, TemplateView


def index(request):
    return render(request, 'index.html', {'answers': Answers.objects.all(), 'quiz_items': Quiz_category.objects.all()})


def materialview(request):
    return render(request, 'materials.html', {'subjects': SubjectMaterial.objects.all(), 'quiz_items': Quiz_category.objects.all()})


class PrivacyTemplateView(TemplateView):
    template_name = 'privacy.html'


class Categories(ListView):
    model = Quiz_category
    template_name = 'index.html'
    context_object_name = 'quiz_items'


class SubjectsDetailView(DetailView):
    model = Quiz_category
    template_name = 'quizzes.html'
    context_object_name = 'quiz_items'


class SubjectMaterialListView(ListView):
    model = SubjectMaterial
    template_name = 'materials.html'
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['item'] = Quiz_category.objects.filter(item=self.object.category_name)
        return context
