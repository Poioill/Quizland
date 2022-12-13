# Generated by Django 4.1.4 on 2022-12-12 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_quiz_category', to='quiz.quiz_category'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(max_length=250),
        ),
    ]
