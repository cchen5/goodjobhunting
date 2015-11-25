# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailnotifs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='email',
            name='recipient',
            field=models.ForeignKey(related_name='recipient', to='emailnotifs.EmailAddress'),
        ),
        migrations.AlterField(
            model_name='email',
            name='sender',
            field=models.ForeignKey(related_name='sender', to='emailnotifs.EmailAddress'),
        ),
        migrations.AlterUniqueTogether(
            name='emailaddress',
            unique_together=set([('address',)]),
        ),
    ]
