# Generated by Django 2.2 on 2022-03-20 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Students'},
        ),
    ]
