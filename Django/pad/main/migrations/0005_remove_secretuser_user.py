# Generated by Django 4.1.7 on 2023-03-25 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_secretuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secretuser',
            name='user',
        ),
    ]
