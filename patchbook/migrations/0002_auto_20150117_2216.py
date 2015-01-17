# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patchbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='automate',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instrument',
            name='length',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instrument',
            name='ouput',
            field=models.CharField(default=b'LR', max_length=2, choices=[(b'LR', b'LR'), (b'L', b'L'), (b'R', b'R'), (b'', b'Off')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instrument',
            name='table',
            field=models.ForeignKey(blank=True, to='patchbook.Table', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instrument',
            name='type',
            field=models.CharField(default=b'Pulse', max_length=5, choices=[(b'Pulse', b'Pulse'), (b'Wave', b'Wave'), (b'Kit', b'Kit'), (b'Noise', b'Noise')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='InstrumentType',
        ),
    ]
