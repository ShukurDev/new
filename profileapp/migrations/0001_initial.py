# Generated by Django 3.2.9 on 2021-11-15 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='first name')),
                ('last_name', models.CharField(max_length=32, verbose_name='last name')),
                ('email', models.CharField(max_length=32, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('self_detail', models.TextField(verbose_name='self detail')),
                ('avatar', models.ImageField(upload_to='images')),
                ('purpose', models.CharField(max_length=128, verbose_name='purpose')),
                ('portfolio', models.FileField(upload_to='files/portfolio')),
                ('teacher_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='techers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='last name')),
                ('email', models.CharField(blank=True, max_length=32, null=True, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('self_detail', models.TextField(verbose_name='self detail')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images')),
                ('purpose', models.CharField(max_length=128, verbose_name='purpose')),
                ('interests', models.CharField(max_length=128, verbose_name='interests')),
                ('student_course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courseapp.coursemodel')),
                ('student_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]