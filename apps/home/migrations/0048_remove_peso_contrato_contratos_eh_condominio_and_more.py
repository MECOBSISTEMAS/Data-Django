# Generated by Django 4.2.3 on 2023-09-06 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_alter_peso_contrato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peso',
            name='contrato',
        ),
        migrations.AddField(
            model_name='contratos',
            name='eh_condominio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contratos',
            name='vendedores',
            field=models.ManyToManyField(blank=True, related_name='contratos_como_vendedores', to='home.pessoas'),
        ),
        migrations.AddField(
            model_name='peso',
            name='parcela',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pesos', to='home.contratoparcelas'),
        ),
    ]