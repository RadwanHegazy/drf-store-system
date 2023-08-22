from django.contrib import admin
from .models import CustomUser, ProductModel, CartModel, PaymenyModel
from django.contrib.auth.models import Group



# Panels

class ProductPanel (admin.ModelAdmin) : 
    list_display = ['title','price','quantity']
    search_fields = ['title']
    readonly_fields = ['Image']
    ordering = ['quantity']
    

class PaymentPanel (admin.ModelAdmin) : 
    list_display = ['user','price','isDone']



class CustomUserPanel (admin.ModelAdmin) : 
    list_display = ['username','email','country']
    search_fields = ['username']
    list_filter = ['gender','country']



# register on admin

admin.site.register(ProductModel, ProductPanel)
admin.site.register(PaymenyModel, PaymentPanel)
admin.site.register(CustomUser, CustomUserPanel)
admin.site.register(CartModel)



# un register from admin
admin.site.unregister(Group)