# Generated by Django 4.1.1 on 2023-03-11 05:31

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_blog_delete_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='photo1',
            field=models.ImageField(upload_to='properties/'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='photo2',
            field=models.ImageField(upload_to='properties/'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='photo3',
            field=models.ImageField(upload_to='propeeties/'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='photo4',
            field=models.ImageField(upload_to='properties/'),
        ),
    ]
