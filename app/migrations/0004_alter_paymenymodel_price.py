# Generated by Django 4.0 on 2023-08-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_paymenymodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenymodel',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
