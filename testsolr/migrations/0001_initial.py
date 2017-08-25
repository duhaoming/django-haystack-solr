# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 05:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(choices=[('collie', 'Collie'), ('labrador', 'Labrador'), ('pembroke', 'Pembroke Corgi'), ('shetland', 'Shetland Sheepdog'), ('border', 'Border Collie')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('owner_last_name', models.CharField(blank=True, max_length=255)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('bio', models.TextField(blank=True)),
                ('public', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toys', to='testsolr.Dog')),
            ],
        ),
    ]