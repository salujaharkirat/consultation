# Generated by Django 3.0.3 on 2020-03-01 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authservice', '0001_initial'),
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assistant',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='assistant',
            name='email',
        ),
        migrations.RemoveField(
            model_name='assistant',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='assistant',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='assistant',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='assistant',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='authservice.User'),
        ),
    ]