# Generated by Django 3.2.16 on 2023-02-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_calculo_repasse_repasse_calc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vendedor', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('id_contrato', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('vendedor', models.CharField(blank=True, max_length=100, null=True, verbose_name='')),
                ('comprador', models.CharField(blank=True, max_length=100, null=True, verbose_name='')),
                ('nu_parcela', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('vl_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('dt_vencimento', models.DateField(blank=True, null=True, verbose_name='')),
                ('dt_credito', models.DateField(blank=True, null=True, verbose_name='')),
                ('banco', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('contrato', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('evento', models.CharField(blank=True, max_length=128, null=True, verbose_name='')),
                ('deposito', models.CharField(max_length=50, verbose_name='')),
                ('calculo', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('taxas', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('adi', models.CharField(blank=True, max_length=12, null=True, verbose_name='')),
                ('me', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('op', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('repasses', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='')),
                ('comissao', models.CharField(blank=True, max_length=128, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'Dado',
                'verbose_name_plural': 'Dados',
            },
        ),
    ]
