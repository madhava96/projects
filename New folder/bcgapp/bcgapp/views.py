from django.shortcuts import render
from .models import empdata,log
# Create your views here.
def empform(request):
    if request.method=='GET':
        empdat=empdata.objects.all().values()
        return render(request,'bcgapp/empdetailsform.html',{'empdat':empdat})
    else:
        empdata(
            empid=request.POST.get('eid'),
            empname=request.POST.get('ename'),
            doj=request.POST.get('doj'),
            expsalary=request.POST.get('esal'),
            prevexp=request.POST.get('prevexp'),
            designation=request.POST.get('desg')
        ).save()
        empdat=empdata.objects.all().values()
        return render(request,'bcgapp/empdetailsform.html',{'empdat':empdat})
    
    
def adminp(request):
    if request.method=='GET':
        empdat=empdata.objects.all().values()
        return render(request,'bcgapp/adminp.html',{'empdat':empdat})
    else:
        empdata(
            empid=request.POST.get('eid'),
            empname=request.POST.get('ename'),
            doj=request.POST.get('doj'),
            expsalary=request.POST.get('esal'),
            prevexp=request.POST.get('prevexp'),
            designation=request.POST.get('desg')
        ).save()
        empdat=empdata.objects.all().values()
        return render(request,'bcgapp/adminp.html',{'empdat':empdat})
    
def login(request):
        if request.method=='POST':
            un=request.POST.get('uname')
            pd=request.POST.get('pwd')
        # user=authenticate(username=un,password=pd)
            if un=='hr2023@brightcomgroup.com' and pd== 'admin':
                empdat=empdata.objects.all().values()
                return render(request,'bcgapp/adminp.html',{'empdat':empdat})
            else:
                return render(request,'bcgapp/login.html')
        else:
            return render(request,'bcgapp/login.html')
    
def register(request):
    return render(request,'bcgapp/registration.html')