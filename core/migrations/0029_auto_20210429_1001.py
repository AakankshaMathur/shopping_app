# Generated by Django 3.1 on 2021-04-29 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210406_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_quantity',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order')),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product')),
            ],
        ),
    ]
