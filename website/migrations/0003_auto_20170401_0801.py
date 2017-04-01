# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_founder_hours_wanted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(choices=[('EECS', 'Electrical Engineering and Computer Science'), ('IEOR', 'Industrial Engineering and Operations Research'), ('ECON', 'Economics'), ('AMATH', 'Applied Math'), ('CHEM', 'Chemistry'), ('PHYS', 'Physics'), ('MECH', 'Mechanical Engineering'), ('BIOE', 'Bioengineering'), ('CS', 'Computer Science'), ('STAT', 'Statistics'), ('HAAS', 'Business'), ('UND', 'Undecided'), ('NONE', 'Other')], default='UND', max_length=4),
        ),
    ]