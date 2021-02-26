# Generated by Django 3.1 on 2021-02-26 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210226_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customeraddress', to='core.address'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.ManyToManyField(to='core.Address'),
        ),
    ]
