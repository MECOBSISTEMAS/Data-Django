# Generated by Django 3.2.16 on 2023-05-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_repasseretido_aprovada_para_repasse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repasseaprovado',
            name='dado',
        ),
        migrations.AddField(
            model_name='repasseaprovado',
            name='dados',
            field=models.ManyToManyField(blank=True, to='home.Dado'),
        ),
    ]
