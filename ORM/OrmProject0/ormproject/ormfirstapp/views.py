from django.shortcuts import render,redirect

# Create your views here.
from .models import Emp


def homef(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        age=request.POST.get('age')
        address=request.POST.get('address')
        e=Emp()
        e.name=name
        e.email=email
        e.contact=contact
        e.age=age
        e.address=address
        e.save()
        return redirect('/')
    else:    
        return render(request,'addemp.html')

from .form import EmpForm    
def add_emp2(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm
        d={'form':f}
        return render(request,'addemp2.html',d)
