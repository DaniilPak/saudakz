# Generated by Django 3.2.8 on 2021-11-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silkapp', '0004_rename_slug_name_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]