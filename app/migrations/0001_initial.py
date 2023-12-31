# Generated by Django 4.2.7 on 2023-11-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_laptop', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=20)),
                ('memori_internal', models.CharField(max_length=20)),
                ('processor', models.CharField(max_length=100)),
                ('layar', models.CharField(max_length=20)),
                ('harga', models.IntegerField()),
                ('baterai_mAh', models.IntegerField()),
            ],
        ),
    ]
