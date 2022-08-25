# Generated by Django 4.0.7 on 2022-08-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('phoneNumber', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('cardNumber', models.CharField(blank=True, max_length=20, null=True, verbose_name='Card Number')),
                ('cardName', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name on Card')),
                ('cardExp', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Clients',
                'ordering': ('-created',),
            },
        ),
    ]
