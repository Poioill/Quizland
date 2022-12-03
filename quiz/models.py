from django.db import models


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

    def __str__(self):
        return self.category_name


'''class Subject(models.Model):
    subject_name = models.CharField(max_length=40)
    description = models.TextField()
    an_svg = models.ImageField(upload_to='svg/')
    
    def __str__(self):
        return self.subject_name'''
