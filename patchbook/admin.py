from django.contrib import admin
from patchbook.models import PatchSet, Table, TableRow, Wave, WavePosition, Instrument, Tag, InstrumentTag, PatchSetTag
# Register your models here.

admin.site.register(PatchSet)
admin.site.register(Instrument)
admin.site.register(Table)
admin.site.register(TableRow)
admin.site.register(Wave)
admin.site.register(WavePosition)
admin.site.register(Tag)
admin.site.register(InstrumentTag)
admin.site.register(PatchSetTag)
