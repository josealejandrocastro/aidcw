# Generated by Django 2.1.7 on 2019-02-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memoria',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre'),
        ),
    ]