# Generated by Django 4.1.3 on 2022-12-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0018_rename_beforecategories_introductioncategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introductioncategories',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='mainpageinfo',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
