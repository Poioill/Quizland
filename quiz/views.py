from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import CommentsForm
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin


def index(request):
    return render(request, 'index.html', {'answers': Answers.objects.all(),
                                          'quiz_items': Quiz_category.objects.all(),
                                          'footer_info': FooterInformation.objects.all(),
                                          'main_page': MainPageInfo.objects.all(),
                                          'intro': IntroductionCategories.objects.all(),
                                          })


def materialview(request):
    return render(request, 'materials.html', {'subjects': SubjectMaterial.objects.all(),
                                              'quiz_items': Quiz_category.objects.all(),
                                              'languages': LanguagesMaterial.objects.all(),
                                              'literature': LiteratureMaterial.objects.all(),
                                              'footer_info': FooterInformation.objects.all()})


class PrivacyTemplateView(TemplateView):
    template_name = 'privacy.html'


class TermsOfServiceTemplateView(TemplateView):
    template_name = 'service.html'


class Categories(ListView):
    model = Quiz_category
    template_name = 'index.html'
    context_object_name = 'quiz_items'


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.sucess_url, self.object.id)


class SubjectsDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Quiz_category
    template_name = 'quizzes.html'
    context_object_name = 'quiz_items'
    form_class = CommentsForm
    success_msg = 'Added'

    def get_success_url(self):
        return reverse_lazy('subjects', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.comment = self.get_object()
        self.object.save()
        return super().form_valid(form)


class SubjectMaterialListView(ListView):
    model = SubjectMaterial
    template_name = 'materials.html'
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['item'] = Quiz_category.objects.filter(item=self.object.category_name)
        return context
