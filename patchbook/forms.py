from django.forms import ModelForm
from patchbook.models import PatchSet


class PatchSetForm(ModelForm):
    class Meta:
        model = PatchSet
        fields = ['name', 'comments']

