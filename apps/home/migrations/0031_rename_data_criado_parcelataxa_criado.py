# Generated by Django 3.2.16 on 2023-05-10 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_dado_criado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcelataxa',
            old_name='data_criado',
            new_name='criado',
        ),
    ]
