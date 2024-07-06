from django.shortcuts import render, redirect
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

def add_to_cart(request, product_id):
    if request.method == "POST" and product_id : #? if the user is sending a new product
        data = request.POST.dict() #? converts the request data to a dictionary
        size = data.get('size') #? used get instead of ['size] as it wont return a error
        color_id = data.get('color')
        if not size:
            return redirect('store')
        #!getting the client
        if request.user.is_authenticated:
            client = request.user.client
        else :
            return redirect('store')
        order, created = Order.objects.get_or_create(client=client, finished=False)
        item_stock = ItemStock.objects.get(product__id=product_id, size=size, color=color_id) #? In the forms we enter the color, id, and the size
        item_ordered, created = OrderedItem.objects.get_or_create(order=order, itemstock=item_stock) #? adding the product to the cart
        item_ordered.quantity += 1
        item_ordered.save() #? Must save changes made directly to a element
        return redirect('cart')
    else :
        return redirect('store') #? redirect the user to the store if he didn't choose a product

def remove_from_cart(request, product_id) :
    if request.method == "POST" and product_id : #? if the user is sending a new product
        data = request.POST.dict() #? converts the request data to a dictionary
        size = data.get('size') #? used get instead of ['size] as it wont return a error
        color_id = data.get('color')
        if not size:
            return redirect('store')
        #!getting the client
        if request.user.is_authenticated:
            client = request.user.client
        else :
            return redirect('store')
        order, created = Order.objects.get_or_create(client=client, finished=False)
        item_stock = ItemStock.objects.get(product__id=product_id, size=size, color=color_id) #? In the forms we enter the color, id, and the size
        item_ordered, created = OrderedItem.objects.get_or_create(order=order, itemstock=item_stock) #? adding the product to the cart
        item_ordered.quantity -= 1 #? only difference is that we are removing a item from the cart
        item_ordered.save() #? Must save changes made directly to a element
        if item_ordered.quantity <= 0 :
            item_ordered.delete()
        return redirect('cart')
    else :
        return redirect('store') #? redirect the user to the store if he didn't choose a product

def cart(request): 
    if request.user.is_authenticated:
        client = request.user.client
    
    order, created = Order.objects.get_or_create(client=client, finished=False) 
    items_ordered = OrderedItem.objects.filter(order = order)
    context = {"order" : order, "items_ordered" : items_ordered}
    return render(request, 'cart.html', context) 

def checkout(request): 
    return render(request, 'checkout.html') 

def your_account(request): 
    return render(request, 'user/your_account.html') 

def login(request): 
    return render(request, 'user/login.html') 

def view_product(request, product_id, id_color = None) :
    has_stock = False
    sizes = {}
    colors = {} #? needs to be declared
    selected_color = None
    product = Product.objects.get(id=product_id) #? id parameter is created automatically by django
    item_stock = ItemStock.objects.filter(product = product, quantity__gt = 0) #? gets the product that has more than 0 quantity (queryset lookup)
    if len(item_stock) > 0 : 
        has_stock = True #? necessary in order to do a if on the html. if the product is out of stock, will show "Out of Stock"
        colors = {item.color for item in item_stock} #? gets the colors of all products, uses sets '{}' to avoid duplicate colors
        if id_color :
            selected_color = Color.objects.get(id = id_color) #? gets the color object from the Color class
            item_stock = ItemStock.objects.filter(product = product, quantity__gt = 0, color__id = id_color) #? gets the color id  attribute from the Color class (that is automatically created)
            sizes = {item.size for item in item_stock} #? gets the sizes of all products
    context = {'product': product, "has_stock" : has_stock, "colors" : colors, "sizes" : sizes, "selected_color" : selected_color}
    return render(request, 'view_product.html', context)

#! Always when a user creates a account on the website we will create a client for him

