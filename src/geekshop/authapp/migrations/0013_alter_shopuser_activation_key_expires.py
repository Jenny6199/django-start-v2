# Generated by Django 3.2.10 on 2022-01-30 19:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 19, 59, 35, 90754, tzinfo=utc)),
        ),
    ]
