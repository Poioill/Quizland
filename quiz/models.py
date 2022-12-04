from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Answers(models.Model):
    question = models.CharField(max_length=50)
    answer = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.question


class Quiz_category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cat = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Category')

    def __str__(self):
        return self.category_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=40)
    description = models.TextField()
    an_svg = models.FileField(upload_to='svg/', validators=[FileExtensionValidator(['svg', 'pdf', 'doc'])])
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'name': self.})
