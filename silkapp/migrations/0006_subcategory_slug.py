# Generated by Django 3.2.8 on 2021-12-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silkapp', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
