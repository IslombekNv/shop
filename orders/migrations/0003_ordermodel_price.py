# Generated by Django 3.2 on 2021-06-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_ordermodel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]