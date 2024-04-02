# Static Archives

Now we will create a folder for our static archives (midia, css, js) inside the main ecommerce project folder. Inside the folder 'static' we will create other three folders:

* css
* images
* js

In order to load the information of the static files into the html files we will add the following line of code below the {% extends 'base.html' %} in every html file

```html
{% load static %}
```

Obs: it is necessary to put this code in every file as it is used by django to load data instead of only visualizing it to the user.

Afterwards, in the settings.py file we will specify the directory of the static files as django won't automatically search for them

```python
import os # put this in the beginning of the file
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/' #? the link where the static files are hosted

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

Next, we will create a css file on the css folder which will be referenced on the base html file:

```html
<title>Ecommerce Reserva</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
```

Now, we will create a navigation bar. For organization purposes we will create a new html file 'navbar.html' on the templates folder that will contain the code for the navbar. We performed this approach as later on the navigation bar will become very complex and it will be best practice to separate large segments of code into other files.

```html
<nav>
    <a href = "{% url 'homepage' %}">Reserva</a>
    <a href = "{% url 'store' %}">Store</a>
    <a href = "{% url 'login' %}">Login</a>
    <a href = "{% url 'your_account' %}">My Account</a>
    <a href = "{% url 'cart' %}">Cart</a>
</nav>
```

Note that the checkout url wasnt mentioned as it will be acessed from the cart url.

```html
{% block body %}

<h3>Cart</h3>

<a href = "{% url 'checkout' %}">Checkout</a>

{% endblock %}
```

Now we will include the separate navigation bar file on the base html:

```html
<body>
    {% include 'navbar.html' %}
    {% block body %} 
    {% endblock %} 
</body>
```
