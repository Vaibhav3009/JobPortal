# Generated by Django 3.0.9 on 2021-05-18 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('joblocation_address', models.CharField(blank=True, max_length=200, null=True)),
                ('jobtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(default=None, null=True)),
            ],
            options={
                'db_table': 'job_post',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'job_applied',
                'managed': True,
            },
        ),
    ]
