# Generated by Django 5.0.3 on 2024-03-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_carousel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='subtitle',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='ima/'),
        ),
    ]
