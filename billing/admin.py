from django.contrib import admin
from .models import Customer


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_id', 'created_at', 'updated_at')

    '''filter options'''
    list_filter = ('customer_id',)

    '''10 items per page'''
    list_per_page = 10


admin.site.register(Customer, CustomerAdmin)
