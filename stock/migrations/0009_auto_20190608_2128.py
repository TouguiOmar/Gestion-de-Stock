# Generated by Django 2.2.1 on 2019-06-08 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_detailcommande_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devis',
            name='Date_Devis',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
