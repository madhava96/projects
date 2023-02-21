from django.shortcuts import render
from django.http import HttpResponse
from .models import empdata,log
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'bcgapp/homepage.html')
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
        sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
        return render(request,'bcgapp/adminp.html',{'empdat':empdat, 'sortedUrl': sortedUrl})
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
        sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
        return render(request,'bcgapp/adminp.html',{'empdat':empdat, 'sortedUrl': sortedUrl})
    
def login(request):

    if request.method=='POST':
        un=request.POST.get('uname')
        pd=request.POST.get('pwd')
        sort_flag = request.POST.get('sort_flag')
        # user=authenticate(username=un,password=pd)
        if un=='hr2023@brightcomgroup.com' and pd== 'admin':
            
            empdat=empdata.objects.all().values()
            sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
            return render(request,'bcgapp/empdetailsform.html',{'empdat':empdat, 'sortedUrl': sortedUrl})
        else:
            empdata(
            empid=request.POST.get('eid'),
            empname=request.POST.get('ename'),
            doj=request.POST.get('doj'),
            expsalary=request.POST.get('esal'),
            prevexp=request.POST.get('prevexp'),
            designation=request.POST.get('desg')
        ).save()
            return render(request,'bcgapp/empdetailsform.html')
           
    else:
         return render(request,'bcgapp/login.html')
        
            
def register(request):
    return render(request,'bcgapp/registration.html')

def man(request):
    if request.method=='POST':
        un=request.POST.get('mname')
        pd=request.POST.get('mpwd')
        if un=='manager@brightcomgroup.com' and pd== 'admin':
            empdat=empdata.objects.all().values()
            sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
            return render(request,'bcgapp/adminp.html',{'empdat':empdat, 'sortedUrl': sortedUrl})
        else:
            return render(request,'bcgapp/manager.html')
    return render(request,'bcgapp/manager.html')


def get_res(request):
    # print("FLagging", flag)

    if request.method == "GET":
        sort_flag = request.GET.get('s_flag')
        print("FLagging", request.path)

        if sort_flag == "asc":
            data = empdata.objects.all().order_by('empid').values()
            sortedUrl = "http://localhost:8000/employees/?s_flag=desc"
        else:
            data = empdata.objects.all().order_by('-empid').values()
            sortedUrl = "http://localhost:8000/employees/?s_flag=asc"

    return render(request,'bcgapp/adminp.html',{'empdat':data, 'sortedUrl': sortedUrl})