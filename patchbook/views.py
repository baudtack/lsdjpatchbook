from django.shortcuts import render
from django.http import HttpResponse
from patchbook.models import PatchSet, PatchSetForm, Instrument, InstrumentForm, Table, TableForm, TableRow, TableRowForm
from datetime import datetime

def index(request):
    return HttpResponse("LSDJ Patch Book!")

def patchset(request, patchset_id):
    return HttpResponse("You're looking at patch set %s." % patchset_id)

def patchset_create_or_update(request):
    if(request.method == 'GET'):
        form = PatchSetForm(request.GET)
        instrument_form = InstrumentForm(request.GET)
        table_form = TableForm(request.GET)
        table_rows = [TableRowForm(initial={'position': str(i),
                                            'vol': '00',
                                            'tsp': '00',
                                            'cmd1_setting': '00',
                                            'cmd2_setting': '00'
                                             }) for i in xrange(16)]

    else:

        form = PatchSetForm(request.POST)
        instrument_form = InstrumentForm(request.POST)
        table_form = TableForm(request.POST)
        table_rows = []
        if form.is_valid():
            form.save()
            if instrument_form.is_valid():
                instrument_form.save();
                if table_form.is_valid():
                    table = table_form.save();
                    for i in xrange(16):
                        tr = TableRow()
                        tr.table = table
                        tr.position = request.POST.getlist('position')[i]
                        tr.vol = request.POST.getlist('vol')[i]
                        tr.tsp = request.POST.getlist('tsp')[i]
                        tr.cmd1 = request.POST.getlist('cmd1')[i]
                        tr.cmd1_setting = request.POST.getlist('cmd1_setting')[i]
                        tr.cmd2 = request.POST.getlist('cmd2')[i]
                        tr.cmd2_setting = request.POST.getlist('cmd2_setting')[i]
                        tr.clean_fields()
                        tr.save()
                    return HttpResponse("create all the things!")
                else:
                    raise Exception(table_form.errors)
            else:
                raise Exception(instrument_form.errors)
        else:
            raise Exception(form.errors)

    return render(request, 'patchset/form.html', { 'form': form,
                                                   'instrument_form': instrument_form,
                                                   'table_form': table_form,
                                                   'table_rows': table_rows})


def instrument(request, instrument_id):
    return HttpResponse("You're looking at instrument %s." % instrument_id)

