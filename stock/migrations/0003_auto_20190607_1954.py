# Generated by Django 2.2.1 on 2019-06-07 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_detaildevis_devis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devis',
            old_name='Date_Commande',
            new_name='Date_Devis',
        ),
    ]