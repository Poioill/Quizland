from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Answers(models.Model):
    question = models.CharField(max_length=50, null=True)
    answer = models.TextField(null=True)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.question


class Quiz_category(models.Model):
    category_name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='', null=True)
    an_svg = models.FileField(null=True, upload_to='svg/', validators=[FileExtensionValidator(['svg', 'pdf', 'doc'])])

    def __str__(self):
        return self.category_name


class SubjectArea(models.Model):
    area = models.ForeignKey(Quiz_category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubjectMaterial(models.Model):
    subject = models.ForeignKey(Quiz_category, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.topic
