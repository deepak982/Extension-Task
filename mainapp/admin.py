from django.contrib import admin
from .models import * 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','created_at','updated_at')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','email_token','is_verify')

class DataAdmin(admin.ModelAdmin):
    list_display = ('intensity', 'topic' ,'region', 'start_year', 'end_year',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(data, DataAdmin)