# Generated by Django 3.2.16 on 2023-05-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_repasseretido_aprovada'),
    ]

    operations = [
        migrations.AddField(
            model_name='dado',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=''),
        ),
    ]
