# Generated by Django 2.2.6 on 2020-08-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0005_furniture_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='color',
        ),
        migrations.AddField(
            model_name='furniture',
            name='breath',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='furniture',
            name='height',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='furniture',
            name='length',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
