from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .managers import CustomUserManager
from django.utils.html import mark_safe
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('Phone Number'), unique=True,max_length=20)
    gender = models.CharField(_('Gender'),choices=(('Male','Male'),('Female','Female')),max_length=10)
    country = models.CharField(_('Country'),max_length=100)
    addresse = models.TextField(max_length=1000)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email




class ProductModel (models.Model) : 
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='products-images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    def Image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

    def __str__(self) : 
        return f'{self.title}'
    
    class Meta:
        ordering = ('-created_at',)


class CartModel (models.Model) :
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self) : 
        return f'{self.product}'
    

class PaymenyModel (models.Model) :
    products = models.ManyToManyField(ProductModel)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    price = models.FloatField()
    isDone = models.BooleanField(default=False)

    def __str__(self) : 
        return f'{self.user.username} buy {self.products.count()} prodcuts with {self.price}EGP'
    



@receiver(post_save, sender = CustomUser)
def CreateTokenForEachUser (created, instance, **args) : 
    if created: 
        Token.objects.create( user = instance)

