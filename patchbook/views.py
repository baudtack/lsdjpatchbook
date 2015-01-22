from django.shortcuts import render
from django.http import HttpResponse
from patchbook.models import PatchSet, PatchSetForm, Instrument, InstrumentForm
from datetime import datetime

def index(request):
    return HttpResponse("LSDJ Patch Book!")

def patchset(request, patchset_id):
    return HttpResponse("You're looking at patch set %s." % patchset_id)

def patchset_create_or_update(request):
    if(request.method == 'GET'):
        form = PatchSetForm(request.GET)
        instrument_form = InstrumentForm(request.GET)
    else:
        form = PatchSetForm(request.POST)
        instrument_form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            if instrument_form.is_valid():
                instrument_form.save();
                return HttpResponse("create all the things!")
    return render(request, 'patchset/form.html', { 'form': form,
                                                   'instrument_form': instrument_form })


def instrument(request, instrument_id):
    return HttpResponse("You're looking at instrument %s." % instrument_id)

