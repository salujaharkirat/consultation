# Generated by Django 3.0.3 on 2020-03-03 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20200303_0658'),
        ('doctor', '0002_auto_20200303_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.Office'),
        ),
    ]