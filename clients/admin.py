from django.contrib import admin
from .models import Clients


class ClientAdmin(admin.ModelAdmin):
    list_display=['user','get_user_email','get_subsidiary_name','get_organization_name']
    
    
    def get_user_email(self,obj):
        return obj.user.email
    get_user_email.short_description='Email'
    
    def get_subsidiary_name(self,obj):
        return obj.subsidiary.organization.name+" -> "+obj.subsidiary.name
    get_subsidiary_name.short_description="Belong To"
    
    def get_organization_name(self,obj):
        return obj.organization_name
    get_organization_name.short_description="Organization"
    
admin.site.register(Clients,ClientAdmin)