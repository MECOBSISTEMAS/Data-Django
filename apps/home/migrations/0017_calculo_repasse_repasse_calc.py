# Generated by Django 3.2.16 on 2023-02-15 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_rename_nu_parcelas_calculo_repasse_nu_parcela'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculo_repasse',
            name='repasse_calc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name=''),
        ),
    ]
