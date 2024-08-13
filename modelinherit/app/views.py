from django.shortcuts import render
from .forms import StuForm,TeacherForm

# Create your views here.
def Student(request):
    if request.method=='POST':
        fm=StuForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
      fm=StuForm()
    return render(request,'stu.html',{'form':fm})

def Teacher(request):
    if request.method=='POST':
        fm=TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
      fm=TeacherForm()
    return render(request,'teach.html',{'form':fm})



