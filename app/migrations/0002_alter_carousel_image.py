# Generated by Django 5.0.3 on 2024-03-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='index_images/'),
        ),
    ]
