# Generated by Django 4.0.4 on 2022-06-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silkapp', '0035_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='rate',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
