from django.shortcuts import render
from django.http import HttpResponse
from patchbook.models import PatchSet, PatchSetForm
from datetime import datetime

def index(request):
    return HttpResponse("LSDJ Patch Book!")

def patchset(request, patchset_id):
    return HttpResponse("You're looking at patch set %s." % patchset_id)

def patchset_create_or_update(request):
    if(request.method == 'GET'):
        form = PatchSetForm(request.GET)
    else:
        form = PatchSetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("create all the things!")
    return render(request, 'patchset/form.html', { 'form': form })


def instrument(request, instrument_id):
    return HttpResponse("You're looking at instrument %s." % instrument_id)

