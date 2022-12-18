from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from accounts.models import CustomUser


class MainPageInfo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    button = models.CharField(max_length=20)


class IntroductionCategories(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)


class Answers(models.Model):
    question = models.CharField(max_length=50, null=True)
    answer = models.TextField(null=True)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Answers'


class Quiz_category(models.Model):
    category_name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='', null=True)
    an_svg = models.FileField(null=True, upload_to='svg/', validators=[FileExtensionValidator(['svg', 'pdf', 'doc'])])
    quiz_1 = models.CharField(null=True, max_length=100)
    quiz_2 = models.CharField(null=True, max_length=100)
    quiz_3 = models.CharField(null=True, max_length=100)

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
    url = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.topic


class LiteratureMaterial(models.Model):
    topic = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', null=True)
    url = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.topic


class LanguagesMaterial(models.Model):
    topic = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', null=True)
    url = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.topic


class Comments(models.Model):
    comment = models.ForeignKey(Quiz_category, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='comments_quiz_category')
    comment_text = models.TextField()
    author_login = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, blank=True, verbose_name='Автор комметария', null=True)
    status = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comments'


class FooterInformation(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=50)
    icon = models.FileField(null=True, upload_to='svg/', validators=[FileExtensionValidator(['svg', 'pdf', 'doc'])])

    def __str__(self):
        return self.name


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)


class TermsOfService(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)


class AboutUsReason(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)


class AboutUsTitle(models.Model):
    pre_title = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)


class AboutUsImages(models.Model):
    image = models.ImageField(upload_to='')


class AboutUsWHY(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)