# Creation of various urls

We will create 6 different links in total:

* Main page
* Store
* Your account
* Login
* Cart
* Checkout

In order to do this we will repeat the same steps shown previously with the creation of the homepage.

1) Defining a url for each page on the urls.py:

```python
urlpatterns = [
    path('', homepage, name="homepage"), #? first parameter is the url, second is what function will be runned at the url, and the third is the internal name of the link used to reference the link regardless of its url domain
    path('store/', store, name="store"), 
    path('youraccount/', your_account, name="your_account"), 
    path('login/', login, name="login"), 
    path('cart/', cart, name="cart"), 
    path('checkout/', checkout, name="checkout"), 
]
```

Defining a function for each page on the views.py (the "your_account" and "login" functions were separated for organization purposes as they are both related to the user and therefore were directed into a separate user folder located inside the templates folder):

```python
# Create your views here.
def homepage(request): #? the first parameter always has to be a request
    return render(request, 'homepage.html') #? returns the homepage

def store(request): 
    return render(request, 'store.html') 

def cart(request): 
    return render(request, 'cart.html') 

def checkout(request): 
    return render(request, 'checkout.html') 



def your_account(request): 
    return render(request, 'user/your_account.html') 

def login(request): 
    return render(request, 'user/login.html') 
```

Creating the html file  for each path

![1712086289692](image/3-Creation-of-various-urls/1712086289692.png)

In order to dinamically edit all html files, we will create a base.html which will contain all the data that will be shared amongst the other html files. As we will only want to change the body section, we will utilize the {% block body %} and {% endblock %} features which allow us to edit those sections individualy while keeping the rest that is outside of the block the same for all html files.

base.html created inside the templates folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecommerce Reserva</title>
</head>
<body>
    {% block body %} 
    {% endblock %} 
</body>
</html>
```

Now we will extend the code of the base file to the all other html files as seen in this code of the cart.html

```html
{% extends 'base.html' %}

{% block body %}

<h3>
    Cart
</h3>

{% endblock %}
```

---
