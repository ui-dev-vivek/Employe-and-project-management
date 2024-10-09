
from django.contrib import admin
from django.urls import path,include 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authapp.urls')),
    path('<str:subsidiary>/', include('subsidiaries.urls')),
    
]

admin.site.site_header = "Project Management"
admin.site.site_title = "Project Management"
admin.site.site_icon = ""
admin.site.index_title ="Project Management"