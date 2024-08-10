from django.shortcuts import render
from .forms import StudentReg
from .models import StuModel

# Create your views here.

def AddShow(request):
    if request.method=='POST':
        fm=StudentReg(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=StuModel(name=nm,email=em,password=ps)
            reg.save()
    else:
        fm=StudentReg()
        stud=StuModel.objects.all()
    return render(request,'addandshow.html',context={'form':fm,'std':stud})


def Update(request):
    return render(request,'update.html' )
