# Generated by Django 4.2.3 on 2023-09-12 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_alter_peso_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peso',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.pessoas'),
        ),
    ]