# Generated by Django 4.0 on 2023-08-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_productmodel_paymenymodel_cartmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenymodel',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
