# Generated by Django 4.0.3 on 2022-04-12 20:09
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conteos',
            fields=[
                ('id', models.BigAutoField(auto_created=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('SERVIDOR', models.CharField(max_length=255)),
                ('CAMARA', models.CharField(max_length=255)),
                ('MARZO', models.CharField(max_length=255)),
                ('ABRIL', models.CharField(max_length=255)),
                ('OTROS', models.CharField(max_length=255)),
                ('VIDEOS', models.CharField(max_length=255)),
                ('MULTAS', models.CharField(max_length=255))
            ],
        ),
    ]
