# Generated by Django 3.2.8 on 2022-01-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silkapp', '0009_auto_20211217_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=1),
        ),
    ]
