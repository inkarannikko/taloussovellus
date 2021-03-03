from django import forms
from django.forms import ModelForm

class UploadFileForm(forms.Form):
    file = forms.FileField()

MONTHS = [
    ('1','Tammi'),
    ('2','Helmi'),
    ('3','Maalis'),
    ('4','Huhti'),
    ('5','Touko'),
    ('6','Kesä'),
    ('7','Heinä'),
    ('8','Elo'),
    ('9','Syys'),
    ('10','Loka'),
    ('11','Marras'),
    ('12','Joulu')
]
class MonthForm(forms.Form):
    wanted_month = forms.CharField(label="Valitse kuukausi",
    widget=forms.Select(choices=MONTHS))
   
