# Generated by Django 4.1.3 on 2023-03-27 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_repasseaprovado_remove_dado_pago_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repasseaprovado',
            name='id_vendedor',
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.pessoas'),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='dado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.dado'),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='data_final',
            field=models.DateField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='data_inicial',
            field=models.DateField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='total_credito',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='total_debito',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='total_repasse',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='total_repasses_retidos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='total_taxa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name=''),
        ),
    ]
