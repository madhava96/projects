from django.contrib import admin
from .models import empdata
# Register your models here.

class adminempdata(admin.ModelAdmin):
    list_display =['empid','empname','doj','expsalary','prevexp','designation']
admin.site.register(empdata, adminempdata)