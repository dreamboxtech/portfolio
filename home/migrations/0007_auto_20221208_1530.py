# Generated by Django 3.0.6 on 2022-12-08 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20221208_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Project'),
        ),
    ]
