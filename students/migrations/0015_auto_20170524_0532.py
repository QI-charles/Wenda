# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-24 05:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_faq_baidu_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='teacher_wegiht',
            new_name='visit_wegiht',
        ),
    ]