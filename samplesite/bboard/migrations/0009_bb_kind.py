# Generated by Django 4.2.1 on 2023-06-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0008_alter_bb_options_alter_bb_order_with_respect_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('B', 'куплю'), ('S', 'продам'), ('C', 'поменяю')], default='S', max_length=1),
        ),
    ]
