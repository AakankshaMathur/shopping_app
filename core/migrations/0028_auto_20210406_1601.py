# Generated by Django 3.1 on 2021-04-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20210405_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
