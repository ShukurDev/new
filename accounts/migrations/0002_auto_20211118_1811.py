# Generated by Django 3.2.9 on 2021-11-18 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='date_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Verified user'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Manager')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=32, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=32, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Super user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=32, verbose_name='last name'),
        ),
    ]