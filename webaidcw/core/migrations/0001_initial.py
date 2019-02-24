# Generated by Django 2.1.5 on 2019-02-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estatuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('documento', models.FileField(upload_to='Estatuto', verbose_name='Estatuto')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
            ],
            options={
                'verbose_name': 'estatuto',
                'verbose_name_plural': 'estatutos',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]