from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, 'index.html', {'answers': Answers.objects.all(), 'quiz_items': Quiz_category.objects.all()})


def privacy(request):
    return render(request, 'privacy.html')


class Categories(ListView):
    model = Quiz_category
    template_name = 'index.html'
    context_object_name = 'quiz_items'


class SubjectsDetailView(DetailView):
    model = Quiz_category
    template_name = 'quizzes.html'
    context_object_name = 'quiz_items'
