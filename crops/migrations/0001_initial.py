# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rainfall', models.FloatField(verbose_name='Annual Rainfall Requirement (ml)')),
                ('ph_low', models.FloatField(verbose_name='Lower pH Bound')),
                ('ph_high', models.FloatField(verbose_name='Higher pH Boung')),
            ],
        ),
        migrations.CreateModel(
            name='CropMinerals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(verbose_name='Percetage Requirement')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=20, verbose_name='Scientific Symbol')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rainfall', models.FloatField()),
                ('ph_low', models.FloatField(verbose_name='Lower pH Bound')),
                ('ph_high', models.FloatField(verbose_name='Higher pH Boung')),
            ],
        ),
        migrations.CreateModel(
            name='RegionMinerals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(verbose_name='Percentage Composition')),
                ('mineral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.Mineral')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.Region')),
            ],
        ),
        migrations.AddField(
            model_name='cropminerals',
            name='mineral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.Mineral'),
        ),
    ]
