# Generated by Django 4.1.7 on 2023-03-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_cadcliente_repasse_semanal'),
    ]

    operations = [
        migrations.AddField(
            model_name='dado',
            name='id_comprador',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name=''),
        ),
    ]