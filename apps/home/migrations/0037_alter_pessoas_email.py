# Generated by Django 3.2.16 on 2023-05-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20230511_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]