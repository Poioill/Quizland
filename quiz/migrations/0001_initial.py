# Generated by Django 4.1.3 on 2022-12-05 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, null=True)),
                ('answer', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=40, null=True)),
                ('description', models.TextField(null=True)),
                ('an_svg', models.FileField(null=True, upload_to='svg/', validators=[django.core.validators.FileExtensionValidator(['svg', 'pdf', 'doc'])])),
            ],
        ),
    ]
