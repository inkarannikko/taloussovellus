from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Account

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
    return render(request,'sites/upload.html')

@permission_required('admin.can_add_log_entry')
def upload(request):
    template = "upload.html"
    prompt = {
        'order': 'Order of the CSV should be date, amount, receiver'
    }
    

    if request.method == "POST":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    if not csv_file.name.endswicth('.csv'):
        messages.error(request,'This is not a csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = ioStringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimeter=';'):
        _,  created=Acount.objects.update_or_create(
            date=column[0],
            amount=float(column[2]),
            receiver=column[5]
        )
    context = {}
    return render(request,template,context)