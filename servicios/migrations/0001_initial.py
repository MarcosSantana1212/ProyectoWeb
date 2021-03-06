# Generated by Django 3.2.7 on 2021-10-26 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=80)),
                ('contenido', models.CharField(max_length=80)),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
    ]
