from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html', {'answers': Answers.objects.all(), 'quiz_items': Quiz_category.objects.all()})


class About_Uni(TemplateView):
    template_name = 'index.html'
