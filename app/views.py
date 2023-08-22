from django.shortcuts import get_object_or_404
from rest_framework import decorators,status,permissions,authentication ,generics, mixins
from .serializers import CartSerizlizer, RegisterSerizlizer, PaymentSerializer,ProdcutSerializer
from rest_framework.response import Response
from .models import CartModel, ProductModel, CustomUser,PaymenyModel
from rest_framework.authtoken.models import Token





class Products (mixins.ListModelMixin,generics.GenericAPIView) :
    queryset = ProductModel.objects.all()
    serializer_class = ProdcutSerializer

    def get (self, request) :
        return self.list(request)
    

@decorators.api_view(['GET'])
def ViewProduct (request,productid) : 
    
    product = get_object_or_404(ProductModel, id = productid)

    serilizer = ProdcutSerializer(product)

    return Response(serilizer.data,status=status.HTTP_200_OK)


class addToCart (mixins.CreateModelMixin, generics.GenericAPIView) : 
    queryset = CartModel.objects.all()
    serializer_class = CartSerizlizer

    permission_classes = [permissions.IsAuthenticated]  
    authentication_classes = [authentication.TokenAuthentication]
    
    def post (self, request) :
        serlizer = self.serializer_class(data=request.data)
        
        if serlizer.is_valid():
            if request.user == serlizer.validated_data['user'] :
                return self.create(request)
            else : 
                return Response(data={'msg':'not authenticated user '},status=status.HTTP_400_BAD_REQUEST)
        return Response(serlizer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class Cart (mixins.ListModelMixin,generics.GenericAPIView) :

    serializer_class = CartSerizlizer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = CartModel.objects.all()

    def get (self, request) :
        cart = CartModel.objects.filter(user=request.user)
        serlizers = self.serializer_class(cart, many=True)
        
        return self.list(request)


@decorators.api_view(['POST',"GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
@decorators.authentication_classes([authentication.TokenAuthentication])
def Checkout (request) : 
    
    if request.method == "GET" :
        paymetns = PaymenyModel.objects.all()
        serializers = PaymentSerializer(paymetns,many=True)

        return Response(serializers.data,status=status.HTTP_200_OK)
    
    if request.method == "POST" : 
        cart = CartModel.objects.filter(user=request.user)


        if cart:        

            price = sum([ i.product.price for i in cart])

            payment_model = PaymenyModel.objects.create(user=request.user,price=price)
            for i in cart:
                payment_model.products.add(i.product)
            
            payment_model.save()

            cart.delete()

            serlizer = PaymentSerializer(payment_model)

            return Response(serlizer.data,status=status.HTTP_201_CREATED)
        return Response(data={'msg':'no items in cart'},status=status.HTTP_404_NOT_FOUND)


class RegisterUser (mixins.CreateModelMixin,generics.GenericAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerizlizer

    def post (self, request) :
        return self.create(request)



@decorators.api_view(['POST'])
def Login (request) :

    email = request.POST['email']
    password = request.POST['password']

    user = CustomUser.objects.filter(email=email)

    if user.count() != 1 :
        return Response(data={'msg':"invalid Email"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    
    user = user.first()

    if not user.check_password(password) : 
        return Response(data={'msg':"invalid Password"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
    token = Token.objects.get( user = user ).key

    return Response(data={'token':token},status=status.HTTP_202_ACCEPTED)
