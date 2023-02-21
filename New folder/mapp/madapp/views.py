from django.shortcuts import render

# Create your views here.
def empdata(request):
    return render(request,'madapp/employee.html')