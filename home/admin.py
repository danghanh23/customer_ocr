from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
admin.site.register(Customer, CustomerAdmin)