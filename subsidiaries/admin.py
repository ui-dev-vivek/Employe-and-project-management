from django.contrib import admin
from subsidiaries.models import Organizations,Subsidiaries,Budget
from django.contrib import messages
from django.http import HttpResponseRedirect
# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name','slug','logo']
    search_fields = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class SubsidiariesAdmin(admin.ModelAdmin):
    list_display = ['name','logo','organization']
    search_fields = ('name','description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']

    

class BudgetAdmin(admin.ModelAdmin):
    list_display = ['subsidiary','year','ammount']
    search_fields = ('subsidiary__name','year')
    # prepopulated_fields = {'slug': ('name',)}
    ordering = ['subsidiary']

    def save_model(self, request, obj, form, change):
        # Check if a budget for the same subsidiary and year already exists
        budget = Budget.objects.filter(subsidiary=obj.subsidiary, year=obj.year).first()

        if budget and budget.pk != obj.pk:        
            return HttpResponseRedirect(request.path)
        super().save_model(request, obj, form, change)
       




admin.site.register(Subsidiaries, SubsidiariesAdmin)
admin.site.register(Budget,BudgetAdmin)
admin.site.register(Organizations,OrganizationAdmin)
