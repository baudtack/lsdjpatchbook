# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patchbook', '0003_auto_20150122_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
