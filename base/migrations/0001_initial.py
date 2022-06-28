# Generated by Django 4.0.3 on 2022-06-24 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='From_Station',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='To_Station',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Train_Route',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('end', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.to_station')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.from_station')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.train')),
            ],
        ),
    ]
