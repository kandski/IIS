# Generated by Django 2.0b1 on 2017-11-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zlodeji', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zlodej',
            name='fotka',
            field=models.CharField(max_length=300),
        ),
    ]