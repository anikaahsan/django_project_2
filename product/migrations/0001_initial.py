# Generated by Django 4.1.6 on 2023-02-09 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
