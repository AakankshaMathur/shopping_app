# Generated by Django 3.1 on 2021-03-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
