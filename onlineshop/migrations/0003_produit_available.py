# Generated by Django 3.0.14 on 2021-05-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_auto_20210515_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
