# Generated by Django 3.2.9 on 2021-12-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True,
                 choices=[('1', 'Tel Aviv'), ('2', 'Jerusalem'), ('3', 'Haifa')],
                  default='1', max_length=15, null=True)),
                ('job_type', models.CharField(blank=True,
                 choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')],
                  default='2', max_length=15, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('post_until', models.DateField()),
                ('is_active', models.BooleanField()),
                ('marked_count', models.IntegerField(default=0)),
                ('apply_link', models.URLField(null=True, unique=True)),
            ],
        ),
    ]
