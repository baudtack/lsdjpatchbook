# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patchbook', '0002_auto_20150117_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrument',
            old_name='ouput',
            new_name='output',
        ),
        migrations.AlterField(
            model_name='instrument',
            name='wave',
            field=models.DecimalField(max_digits=3, decimal_places=1, choices=[(12.5, b'12.5%'), (50, b'50%'), (75, b'75%'), (25, b'25%')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patchset',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
