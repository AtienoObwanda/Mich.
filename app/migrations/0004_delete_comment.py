# Generated by Django 4.0.5 on 2022-06-16 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_project_projectimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
