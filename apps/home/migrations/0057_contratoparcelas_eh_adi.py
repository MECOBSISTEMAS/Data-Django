# Generated by Django 4.2.3 on 2023-09-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_alter_peso_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratoparcelas',
            name='eh_adi',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]