# Generated by Django 2.0b1 on 2017-12-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zlodeji', '0002_auto_20171130_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zlodej',
            name='odmena',
            field=models.IntegerField(default=0),
        ),
    ]
