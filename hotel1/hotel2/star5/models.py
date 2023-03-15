from django.db import models

# Create your models here.
class login(models.Model):
    
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    
#create empdetails.
class GenderField(models.CharField):
    description = "A field to represent gender"
    
    #def __init__(self, *args, **kwargs):
        #kwargs.setdefault('max_length', 1)
        #kwargs.setdefault('choices', [
           # ('M', 'Male'),
            #('F', 'Female'),
        #])
        #super().__init__(*args, **kwargs)


GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class employeedetails(models.Model):
    EMPLOYEE_ID=models.IntegerField(primary_key=True)
    EMPLOYEE_NAME=models.CharField(max_length=30)
    DATE_OF_JOINING=models.CharField(max_length=30)
    SALARY=models.DecimalField(max_digits=7,decimal_places=3)
    MOBILE=models.CharField(max_length=10)
    DESIGNATION=models.CharField(max_length=30)
    GENDER = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)


    
