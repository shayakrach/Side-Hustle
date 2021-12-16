# Generated by Django 3.2.9 on 2021-12-08 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='publisher',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
