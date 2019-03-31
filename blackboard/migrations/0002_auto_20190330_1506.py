# Generated by Django 2.1.3 on 2019-03-30 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blackboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runningsession',
            name='date',
        ),
        migrations.AddField(
            model_name='runningsession',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
