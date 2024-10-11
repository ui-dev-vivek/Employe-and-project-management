from django.contrib import admin
from employees.models import Employees

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['user']


admin.site.register(Employees,EmployeeAdmin)



