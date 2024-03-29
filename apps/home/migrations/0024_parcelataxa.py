# Generated by Django 4.1.3 on 2023-03-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_repasseaprovado_dado'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParcelaTaxa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_contrato', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('comprador', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome do comprador ')),
                ('vendedor', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome do vendedor ')),
                ('parcela', models.CharField(blank=True, max_length=128, null=True, verbose_name='')),
                ('dt_vencimento', models.DateField(blank=True, null=True, verbose_name='')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('tcc', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('desconto_total', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('honorarios', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('repasse', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'ParcelaTaxa',
                'verbose_name_plural': 'ParcelaTaxas',
                'db_table': 'parcela_taxa',
                'managed': True,
            },
        ),
    ]
