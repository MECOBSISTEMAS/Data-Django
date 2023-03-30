# Generated by Django 4.1.3 on 2023-03-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_dado_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepasseAprovado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vendedor', models.CharField(blank=True, max_length=128, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'RepasseAprovado',
                'verbose_name_plural': 'RepasseAprovados',
                'db_table': 'repasses_aprovados',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='dado',
            name='pago',
        ),
        migrations.AddField(
            model_name='dado',
            name='repasse_aprovado',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Essa opção serve para identificar se determinado dado foi aprovado para repasse'),
        ),
    ]