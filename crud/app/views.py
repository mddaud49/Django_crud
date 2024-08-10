from django.shortcuts import render,HttpResponseRedirect
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
            print(nm)
            print(em)
            print(ps)
            reg=StuModel(name=nm,email=em,password=ps)
            reg.save()
            fm=StudentReg()
    else:
        fm=StudentReg()
    stud=StuModel.objects.all()
    return render(request,'addandshow.html',{'form':fm,'std':stud})


def Update(request,id):
    if request.method=='POST':
        pi=StuModel.objects.get(pk=id)
        fm=StudentReg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi=StuModel.objects.get(pk=id)
         fm=StudentReg(instance=pi)
    return render(request,'update.html',{'form':fm})

def DeleteData(request,id):
    if request.method=='POST':
        pi=StuModel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

