# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-04 04:30
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    Profile = apps.get_model("website", "Profile")

    db_alias = schema_editor.connection.alias
    Profile.objects.using(db_alias).filter(position='').update(position='NONE')
    Profile.objects.using(db_alias).filter(role='').update(role='NONE')
    Profile.objects.using(db_alias).filter(year='').update(year='NONE')


def reverse_func(apps, schema_editor):
    Profile = apps.get_model("website", "Profile")

    db_alias = schema_editor.connection.alias
    Profile.objects.using(db_alias).filter(position='NONE').update(position='')
    Profile.objects.using(db_alias).filter(role='NONE').update(role='')
    Profile.objects.using(db_alias).filter(year='NONE').update(year='')


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE',
                          reverse_sql=migrations.RunSQL.noop),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, choices=[('0', 'Partnership'), ('1', 'Paid'), ('NONE', 'Other')], max_length=4, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('MARK', 'Marketing'), ('BIZ', 'Business/Administration'), ('SALE', 'Sales'), ('DES', 'Design'), ('PM', 'Product Manager'), ('CS', 'Software engineer'), ('HARD', 'Hardware engineer'), ('IOS', 'Mobile developer'), ('CONS', 'Consulting'), ('HR', 'Human resources'), ('NONE', 'Other')], default='NONE', max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(blank=True, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate'), ('PH', 'PhD'), ('PD', 'Post-Doc'), ('AL', 'Alumni'), ('NONE', 'Other')], default='NONE', max_length=4, verbose_name='Year'),
        ),
        migrations.RunPython(forwards_func, reverse_func, atomic=True),
        migrations.RunSQL(migrations.RunSQL.noop,
                          reverse_sql='SET CONSTRAINTS ALL IMMEDIATE'),
    ]