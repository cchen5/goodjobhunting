# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=200)),
                ('recipient', models.CharField(max_length=200)),
                ('subject_line', models.CharField(max_length=500)),
                ('email_body', models.CharField(max_length=5000)),
            ],
        ),
    ]
