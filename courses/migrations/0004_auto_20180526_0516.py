# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180526_0505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-created',)},
        ),
        migrations.RemoveField(
            model_name='course',
            name='order',
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
