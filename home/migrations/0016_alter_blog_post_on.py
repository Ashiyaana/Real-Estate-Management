# Generated by Django 4.1.1 on 2023-03-17 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_blog_post_on_alter_properties_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 3, 17)),
        ),
    ]