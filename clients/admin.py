from django.contrib import admin
from .models import Clients


class ClientAdmin(admin.ModelAdmin):
    list_display=['user','get_user_emai']

admin.site.register(Clients,ClientAdmin)