# Generated by Django 4.1.3 on 2023-04-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_parcelataxa_data_criado_parcelataxa_id_comprador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='aprovada',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='debito',
            name='aprovada',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='taxa',
            name='aprovada',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name=''),
        ),
    ]
