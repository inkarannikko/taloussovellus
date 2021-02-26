from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import csv, io
from .forms import UploadFileForm
from django.contrib import messages
from .models import Account
from django.core.files.storage import default_storage
import os




def paavalikko(request):
    return render(request,'sites/paavalikko.html')

def talous(request):
    return render(request,'sites/talous.html')

def sijoitukset(request):
    return render(request,'sites/sijoitukset.html')

def menot(request):
    return render(request,'sites/menot.html')

def tulot(request):
    return render(request,'sites/tulot.html')

def kassavirta(request):
    return render(request,'sites/kassavirta.html')

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request,'This is not a csv file')
            else:
                fs = FileSystemStorage()
                filename = fs.save(csv_file.name, csv_file)
                handle_uploaded_file(filename)
                messages.success(request,'Upload successful')
        return HttpResponseRedirect('/upload')
    else:
        return render(request, 'sites/upload.html')

def change_date_format(d):
    dmy = d.split(".")
    d = dmy[0]
    m = dmy[1]
    y = dmy[2]
    if (len(d) == 1):
        d = '0' + d
    if (len(m) == 1):
        m = '0' + m
    return y + '-' + m + '-' + d

def handle_uploaded_file(file):
    f = default_storage.open(os.path.join(file), 'r')
    counter=0
    for row in f:
        if counter==0:
            counter+=1
            continue
        else:
            counter+=1
            data_set = row.split(";")
            date_ = change_date_format(data_set[0])
            _,  created=Account.objects.update_or_create(
                date=date_,
                amount=float(data_set[2].replace(',','.')),
                receiver=data_set[5]
            )
    f.close()
   
    
