# Generated by Django 4.1.7 on 2023-03-20 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_userpoints_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpoints',
            name='challenges',
        ),
        migrations.AddField(
            model_name='userpoints',
            name='challenges',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.challenge'),
            preserve_default=False,
        ),
    ]
