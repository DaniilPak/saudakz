# Generated by Django 4.0.4 on 2022-05-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silkapp', '0030_notification_initiator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='comment',
            field=models.ManyToManyField(default=None, to='silkapp.commentnrate'),
        ),
    ]
