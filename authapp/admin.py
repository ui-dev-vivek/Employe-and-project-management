from django.contrib import admin
from authapp.models import User
from .forms import MyUserForm

class MyUser(admin.ModelAdmin):
    form = MyUserForm
    list_display=('username','email','is_superuser','is_employee','is_client')
    fieldsets=(
        ('Basic',{'fields':('username','password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('is_employee', 'is_client')}),
    )
    add_fieldsets = (
        ('NEW', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active','is_employee', 'is_client')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username','is_employee','is_client')
    
admin.site.register(User,MyUser)