# Generated by Django 4.1.1 on 2023-05-10 04:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0019_alter_blog_post_on_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 5, 10)),
        ),
    ]
