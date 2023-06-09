# Generated by Django 4.1.1 on 2023-03-10 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_properties_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='no_of_floors',
            field=models.IntegerField(default='no of floors'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='parking',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='parking', max_length=100),
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_for',
            field=models.CharField(choices=[('rent', 'rent'), ('sale', 'sale')], default='property for', max_length=30),
        ),
    ]
