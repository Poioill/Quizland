# Generated by Django 4.1.3 on 2022-12-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_mainpageinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeforeCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
