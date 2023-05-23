# Generated by Django 4.1.1 on 2023-05-03 16:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0018_alter_blog_post_on_alter_properties_area_sqft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 5, 3)),
        ),
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('propertyid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.properties')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
    ]