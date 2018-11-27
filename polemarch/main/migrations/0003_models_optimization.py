# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_modules_and_rename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='inventory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history', related_query_name='history', to='main.Inventory'),
        ),
        migrations.AlterField(
            model_name='history',
            name='kind',
            field=models.CharField(db_index=True, default='PLAYBOOK', max_length=50),
        ),
        migrations.AlterField(
            model_name='history',
            name='status',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='hook',
            name='enable',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='hook',
            name='recipients',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hook',
            name='type',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='hook',
            name='when',
            field=models.CharField(db_index=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='inventory_file',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='schedule',
            field=models.CharField(max_length=768),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default=uuid.uuid1, max_length=251),
        ),
        migrations.AlterField(
            model_name='variable',
            name='key',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterIndexTogether(
            name='history',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='historylines',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='template',
            index_together=set([]),
        ),
    ]
