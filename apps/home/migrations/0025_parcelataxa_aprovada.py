# Generated by Django 4.1.3 on 2023-03-31 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_parcelataxa'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcelataxa',
            name='aprovada',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name=''),
        ),
    ]