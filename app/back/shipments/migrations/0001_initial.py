# Generated by Django 4.0.2 on 2022-02-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('date_shipment', models.DateTimeField(verbose_name='date_shipment')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='date created')),
            ],
        ),
    ]
