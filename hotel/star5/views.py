from django.shortcuts import render ,redirect
from .models import login
from .models import employeedetails
from django.contrib import messages

# Create your views here.
def loginpage(request):
    if request.method == 'GET':
        return render(request,'loginpage.html')
    else: #login authentication
        global username
        username=request.POST.get('username')
        password=request.POST.get('password')
        uname=login.objects.filter(username=username)
        pwd=login.objects.filter(password=password)
        if uname and pwd:
            dsig = login.objects.filter(username=username)
            for i in dsig:
                dsg=i.designation 
                if dsg =='Manager':
                    return render(request,'Managerhomepage.html') 
                if dsg =='Admin':
                    return render(request,'Adminhomepage.html')
                else:
                    return render(request,'Receptionisthomepage.html')
        else:
            messages.success(request,'Invalid Details')
            return render(request,'loginpage.html')

def Managerhomepage(request):
    return render(request,'Managerhomepage.html')
def Adminhomepage(request):
    return render(request,'Adminhomepage.html')
def Receptionisthomepage(request):
    return render(request,'Receptionisthomepage.html')
def table(request):
    return render(request,'table.html')
def employeedata(request):
    return render(request,'employeedata.html')
def hotelmanager(request):
    return render(request,'hotelmanager.html')



def employeeform(request):
    if request.method=='GET':
        return render(request,'employeeform.html')
    else:
       employeedetails(
            EMPLOYEE_ID=request.POST.get('EMPLOYEE_ID'),
            EMPLOYEE_NAME=request.POST.get('EMPLOYEE_NAME'),
            DATE_OF_JOINING=request.POST.get('DATE_OF_JOINING'),
            SALARY=request.POST.get('SALARY'),
            MOBILE=request.POST.get('MOBILENUMBER'),
            DESIGNATION=request.POST.get('DESIGNATION'),
            GENDER=request.POST.get('GENDER')
        ).save()
       return render(request,'employeeform.html')
def check(request):
    return render(request,'Roomavailability.html')
def empdetails(request):
    empdat=employeedetails.objects.all().values()
    return render(request,'empdetails.html',{'empdat':empdat})
def Roomavailability(request):
    return render(request,'Roomavailability.html')
def RoomBooking(request):
    return render(request,'RoomBooking.html')




