# Generated by Django 2.0.1 on 2018-01-16 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='article',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='like',
        ),
    ]
