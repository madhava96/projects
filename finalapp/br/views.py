from django.shortcuts import render,redirect
from django.core import paginator
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import empdata
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

@login_required(login_url='/loginpage/')
#creating views for homepage,loginpage,empform,empdetails
def homepage(request):
    return render(request,'homepage.html')

def loginpage(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else: #login authentication
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('homepage')
        else:
            messages.success(request,'Invalid details!')
            return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('loginpage') 

def empform(request):
    if request.method=='GET':
        empdat=empdata.objects.all().values()  #displaying the values that are before saved 
        return render(request,'empform.html',{'empdat':empdat})  
    else:
        empdata(
            empid=request.POST.get('eid'),
            empname=request.POST.get('ename'),
            doj=request.POST.get('doj'),
            expsalary=request.POST.get('esal'),
            prevexp=request.POST.get('prevexp'),
            designation=request.POST.get('desg')
        ).save()  #saving all the form data in models
        messages.success(request,'Form Submitted Successfully') #displaying the form submitting message
        empdat=empdata.objects.all().values() #displaying the values  after saving
        return render(request,'empform.html',{'empdat':empdat})

def empdetails(request):
    if request.method=='GET':
        empdat = empdata.objects.all()
        page = request.GET.get('page', 1)  #pagination
        paginator = Paginator(empdat, 5)  #displaying 5 rows in a page
        try:
            empdat = paginator.page(page)
        except PageNotAnInteger:
            empdat = paginator.page(1) #if the page is not integer it will be 1
        except EmptyPage:
            empdat = paginator.page(paginator.num_pages)
        sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
        return render(request, 'empdetails.html', { 'empdat': empdat })
    else:
        empdata(
            empid=request.POST.get('eid'),
            empname=request.POST.get('ename'),
            doj=request.POST.get('doj'),
            expsalary=request.POST.get('esal'),
            prevexp=request.POST.get('prevexp'),
            designation=request.POST.get('desg')
            ).save()  #saving all the form data in models
        empdat=empdata.objects.all().values() #displaying the values  saved
        sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
        return render(request,'empdetails.html',{'empdat':empdat, 'sortedUrl': sortedUrl})

