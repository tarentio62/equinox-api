# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('target', models.CharField(max_length=300)),
                ('command', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=200)),
                ('record', models.ForeignKey(to='equinoxapp.Record')),
            ],
        ),
    ]
