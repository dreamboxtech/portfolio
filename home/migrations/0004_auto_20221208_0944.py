# Generated by Django 3.0.6 on 2022-12-08 08:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20221207_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Project Description'),
        ),
    ]