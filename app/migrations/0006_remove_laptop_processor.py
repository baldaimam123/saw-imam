# Generated by Django 4.2.7 on 2023-11-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_laptop_processor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='processor',
        ),
    ]
