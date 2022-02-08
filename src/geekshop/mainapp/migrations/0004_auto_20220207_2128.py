# Generated by Django 3.2.10 on 2022-02-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='активный'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='активна'),
        ),
    ]