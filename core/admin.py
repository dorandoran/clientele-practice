from django.contrib import admin
from .models import Clientele, ID, Sale, Product

class ClienteleAdmin(admin.ModelAdmin):
    fields = ['name', 'last_name', 'age', 'salary', 'photo', 'email', 'date_birth', 'doc_id']
    list_display = ['name', 'last_name', 'age', 'salary']
    list_filter = ['name', 'last_name', 'age', 'salary']
    search_fields = ['last_name', 'age']

class SaleAdmin(admin.ModelAdmin):
    fields = ['sale_number', 'client', 'total', 'products']
    list_display = ['sale_number', 'client', 'total']
    list_filter = ['sale_number', 'client']
    search_fields = ['sale_number', 'client']

admin.site.register(Clientele, ClienteleAdmin)
admin.site.register(ID)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Product)
