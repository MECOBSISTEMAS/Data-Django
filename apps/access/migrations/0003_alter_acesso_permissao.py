# Generated by Django 3.2.16 on 2023-05-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_alter_acesso_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='permissao',
            field=models.CharField(blank=True, choices=[('consulta', 'consulta'), ('alimentacao', 'alimentacao')], default='consulta', max_length=32, null=True, verbose_name='Esse campo serve para identificar as permissões de cada usuario'),
        ),
    ]