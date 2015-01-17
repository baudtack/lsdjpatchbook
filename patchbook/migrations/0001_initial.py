# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('envelope', models.CharField(max_length=2)),
                ('wave', models.DecimalField(max_digits=3, decimal_places=1)),
                ('ouput', models.CharField(max_length=2)),
                ('length', models.CharField(max_length=5)),
                ('sweep', models.CharField(max_length=2)),
                ('vib_type', models.CharField(max_length=10)),
                ('pu2_tune', models.CharField(max_length=2)),
                ('pu_fine', models.CharField(max_length=1)),
                ('automate', models.BooleanField()),
                ('comments', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstrumentTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instrument', models.ForeignKey(to='patchbook.Instrument')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstrumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatchSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatchSetTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patch_set', models.ForeignKey(to='patchbook.PatchSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TableRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('vol', models.CharField(max_length=2)),
                ('tsp', models.CharField(max_length=2)),
                ('cmd1', models.CharField(max_length=1)),
                ('cmd1_setting', models.CharField(max_length=2)),
                ('cmd2', models.CharField(max_length=1)),
                ('cmd2_setting', models.CharField(max_length=2)),
                ('table', models.ForeignKey(to='patchbook.Table')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WavePosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=1)),
                ('value', models.CharField(max_length=1)),
                ('wave', models.ForeignKey(to='patchbook.Wave')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patchsettag',
            name='tag',
            field=models.ForeignKey(to='patchbook.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instrumenttag',
            name='tag',
            field=models.ForeignKey(to='patchbook.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instrument',
            name='table',
            field=models.ForeignKey(to='patchbook.Table'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instrument',
            name='type',
            field=models.ForeignKey(to='patchbook.InstrumentType'),
            preserve_default=True,
        ),
    ]
