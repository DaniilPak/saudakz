# Generated by Django 3.2.8 on 2022-02-03 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('silkapp', '0019_auto_20220203_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageinstance',
            name='img',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
