# Generated by Django 4.2 on 2023-05-17 10:11

import bboard.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_child_human_icecream_icecreamshop_spare_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='price',
            field=models.FloatField(blank=True, null=True, validators=[bboard.models.validate_even], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(error_messages={'min_length': 'Слишком мало символов'}, max_length=50, validators=[django.core.validators.MinLengthValidator(bboard.models.get_min_length)], verbose_name='Товар'),
        ),
    ]
