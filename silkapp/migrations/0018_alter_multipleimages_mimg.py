# Generated by Django 3.2.8 on 2022-02-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silkapp', '0017_multipleimages_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimages',
            name='mimg',
            field=models.ManyToManyField(blank=True, to='silkapp.ImageInstance'),
        ),
    ]