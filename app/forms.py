from django import forms
from django.forms import ModelForm

class UploadFileForm(forms.Form):
    file = forms.FileField()

MONTHS = [
    ('1','Jan'),
    ('2','Feb'),
    ('3','March'),
    ('4','April')

]
class MonthForm(forms.Form):
    wanted_month = forms.CharField(label="Choose a month",
    widget=forms.Select(choices=MONTHS))
   
