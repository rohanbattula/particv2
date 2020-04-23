from django import forms
from .models import Party

class PartyForm(forms.ModelForm):

    class Meta:
        model = Party
        fields = ['name', 'address', 'status', 'distance','entryFee','dateTime','guysAllowed']
