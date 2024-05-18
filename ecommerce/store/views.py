from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request): #? the first parameter always has to be a request
    banners = Banner.objects.filter(active=True)
    context = {"banners" : banners}
    return render(request, 'homepage.html', context) #? returns the homepage

def store(request, category_name = None):
    products = Product.objects.filter(active=True) #? grabbing all products from the database (queryset, result of the search of the database)
    if category_name:
        products = products.filter(category__name = category_name) #? gets the name atribute from the category class and filters it according to the name of the category obtained from the banner
    context = {"products" : products} 
    return render(request, 'store.html', context) 

def cart(request): 
    return render(request, 'cart.html') 

def checkout(request): 
    return render(request, 'checkout.html') 

def your_account(request): 
    return render(request, 'user/your_account.html') 

def login(request): 
    return render(request, 'user/login.html') 

def view_product(request, product_id, id_color = None) :
    product = Product.objects.get(id=product_id) #? id parameter is created automatically by django
    item_stock = ItemStock.objects.filter(product = product, quantity__gt = 0) #? gets the product that has more than 0 quantity (queryset lookup)
    if len(item_stock) > 0 : 
        has_stock = True #? necessary in order to do a if on the html. if the product is out of stock, will show "Out of Stock"
        colors = {item.color for item in item_stock} #? gets the colors of all products, uses sets '{}' to avoid duplicate colors
    else :
        has_stock = False
        colors = {} #? needs to be declared
    context = {'product': product, 'item_stock': item_stock, "has_stock" : has_stock, "colors" : colors}
    return render(request, 'view_product.html', context)