# Generated by Django 2.1.5 on 2019-03-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0026_auto_20190302_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='imagen',
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen10',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 10'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 4'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen5',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 5'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen6',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 6'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen7',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 7'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen8',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 8'),
        ),
        migrations.AddField(
            model_name='albumimagen',
            name='imagen9',
            field=models.ImageField(blank=True, null=True, upload_to='Noticia', verbose_name='Imagen 9'),
        ),
    ]
