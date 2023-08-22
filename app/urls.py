from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    
    # products
    path('',views.Products.as_view()),
    
    # view product
    path('<int:productid>/',views.ViewProduct),
    
    # add to cart
    path('add-to-cart/',views.addToCart.as_view()),

    # view all products in cart
    path('cart/',views.Cart.as_view()),

    # register new user
    path('register/',views.RegisterUser.as_view()),

    # login 
    path('login/',views.Login),

    # checkout
    path('checkout/',views.Checkout)

]
