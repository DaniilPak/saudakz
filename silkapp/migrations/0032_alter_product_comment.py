# Generated by Django 4.0.4 on 2022-05-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silkapp', '0031_alter_product_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='comment',
            field=models.ManyToManyField(blank=True, to='silkapp.commentnrate'),
        ),
    ]
