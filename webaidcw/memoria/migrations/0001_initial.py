# Generated by Django 2.1.7 on 2019-02-22 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_memoria', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de memoria')),
                ('docuemento', models.FileField(upload_to='Memorias', verbose_name='Memoria')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
            ],
            options={
                'verbose_name': 'memoria',
                'verbose_name_plural': 'memorias',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
