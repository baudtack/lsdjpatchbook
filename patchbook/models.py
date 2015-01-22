from django.db import models
from django.forms import ModelForm


class PatchSet(models.Model):
    name = models.CharField(max_length=200)
    comments = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class PatchSetForm(ModelForm):
    class Meta:
        model = PatchSet
        fields = ['name', 'comments']


class Table(models.Model):
    name = models.CharField(max_length=2)

    
class TableRow(models.Model):
    table = models.ForeignKey(Table)
    position = models.IntegerField()
    vol = models.CharField(max_length=2)
    tsp = models.CharField(max_length=2)
    cmd1 = models.CharField(max_length=1)
    cmd1_setting = models.CharField(max_length=2)
    cmd2 = models.CharField(max_length=1)
    cmd2_setting = models.CharField(max_length=2)


class Wave(models.Model):
    name = models.CharField(max_length=2)


class WavePosition(models.Model):
    wave = models.ForeignKey(Wave)
    position = models.CharField(max_length=1)
    value = models.CharField(max_length=1)
    

class Instrument(models.Model):
    LEFT = 'L'
    RIGHT = 'R'
    BOTH = 'LR'
    OFF = ''
    
    OUTPUT_CHOICES = (
        (BOTH, BOTH),
        (LEFT, LEFT),
        (RIGHT, RIGHT),
        (OFF, 'Off'),
    )

    PULSE = 'Pulse'
    WAVE = 'Wave'
    KIT = 'Kit'
    NOISE = 'Noise'

    TYPE_CHOICES = (
        (PULSE, PULSE),
        (WAVE, WAVE),
        (KIT, KIT),
        (NOISE, NOISE),
    )

    WAVE_CHOICES = {
        (12.5, '12.5%'),
        (25, '25%'),
        (50, '50%'),
        (75, '75%'),
    }
        
    name = models.CharField(max_length=5)
    type = models.CharField(max_length=5,
                            choices=TYPE_CHOICES,
                            default=PULSE)
    envelope = models.CharField(max_length=2)
    wave = models.DecimalField(max_digits=3,
                               choices=WAVE_CHOICES,
                               decimal_places=1)
    output = models.CharField(max_length=2,
                             choices=OUTPUT_CHOICES,
                             default=BOTH)
    length = models.CharField(max_length=5, null=True, blank=True)
    sweep = models.CharField(max_length=2)
    vib_type = models.CharField(max_length=10)
    pu2_tune = models.CharField(max_length=2)
    pu_fine = models.CharField(max_length=1)
    automate = models.BooleanField(default=False)
    table = models.ForeignKey(Table, null=True, blank=True)
    comments = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class InstrumentForm(ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'type', 'envelope',
                  'wave', 'output', 'length',
                  'sweep', 'vib_type', 'pu2_tune',
                  'pu_fine', 'automate', 'table',
                  'comments']
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)


class InstrumentTag(models.Model):
    tag = models.ForeignKey(Tag)
    instrument = models.ForeignKey(Instrument)


class PatchSetTag(models.Model):
    tag = models.ForeignKey(Tag)
    patch_set = models.ForeignKey(PatchSet)
