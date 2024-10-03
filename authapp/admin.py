from django.contrib import admin
from authapp.models import User
from django import forms

class MyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_employee', 'is_client')
        
    def __init__(self, *args, **kwargs):
        super(MyUserForm, self).__init__(*args, **kwargs)      
        self.fields['username'].required = True   
        self.fields['email'].required = True      
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True  
        self.fields['is_employee'].required = False 
        self.fields['is_client'].required = False
        self.fields['date_joined'].required=False   

    

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
    search_fields = ('username', 'email')
    ordering = ('username',)
    
admin.site.register(User,MyUser)