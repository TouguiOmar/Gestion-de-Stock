# Generated by Django 2.2.1 on 2019-06-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20190607_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrateur',
            name='Type',
            field=models.IntegerField(default=0),
        ),
    ]
