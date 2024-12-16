from django.shortcuts import render
from .models import Salesdata
from .forms import SalesdataForm
# Create your views here.
def index(request):
    data=Salesdata.objects.all()
    if request.method == 'POST':
        form = SalesdataForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SalesdataForm()
    context ={
        'data':data,
        'form':form,
    }
    return render(request, 'dashboard/index.html',context)