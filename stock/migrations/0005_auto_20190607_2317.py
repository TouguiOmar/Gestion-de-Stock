# Generated by Django 2.2.1 on 2019-06-07 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20190607_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='Valid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='devis',
            name='Valid',
            field=models.IntegerField(default=0),
        ),
    ]
