from django.contrib import admin
from authapp.models import User



class MyUser(admin.ModelAdmin):
    list_display=('username','email','is_superuser','is_employee','is_client')
    fieldsets=(
        ('Basic',{'fields':('username','password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('is_employee', 'is_client')}),
    )
admin.site.register(User,MyUser)