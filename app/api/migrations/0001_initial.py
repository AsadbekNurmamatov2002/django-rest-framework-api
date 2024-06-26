# Generated by Django 5.0.3 on 2024-03-26 06:01

import django.db.models.deletion
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
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='product/%Y/%M/%D/')),
                ('slug', models.SlugField(blank=True, max_length=260)),
            ],
        ),
        migrations.CreateModel(
            name='Xomashyolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('soni', models.IntegerField()),
                ('meter', models.CharField(blank=True, max_length=250, null=True)),
                ('narxi', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Productkx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('xomashyolar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.xomashyolar')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.PositiveIntegerField(default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('xomashyo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.xomashyolar')),
            ],
        ),
    ]
