# Generated by Django 4.0.3 on 2022-06-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_train_route_duration_train_route_price_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pnr_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
