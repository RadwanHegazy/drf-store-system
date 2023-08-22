from rest_framework import serializers
from .models import CustomUser, ProductModel, CartModel, PaymenyModel



class ProdcutSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = ProductModel
        fields = '__all__'


class CartSerizlizer (serializers.ModelSerializer)  :
    class Meta :
        model = CartModel
        fields = '__all__'



class RegisterSerizlizer (serializers.ModelSerializer) :
    password = serializers.CharField(write_only=True)

    class Meta :
        model = CustomUser
        fields = ['id','username','country','gender','phone','email','addresse','password']


class PaymentSerializer (serializers.ModelSerializer) :
    class Meta : 
        model = PaymenyModel
        fields = "__all__"
