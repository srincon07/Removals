# Generated by Django 4.0.7 on 2022-09-07 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('comment', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Furniture Types',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Furniture_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Furniture name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.furniture_type', verbose_name='Type')),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ('-created',),
            },
        ),
    ]
