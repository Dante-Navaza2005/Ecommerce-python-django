from django.urls import path
from .views import * #? Importing everything from the views folder in the same directory

urlpatterns = [
    path('', homepage, name="homepage"), #? first parameter is the url, second is what function will be runned at the url, and the third is the internal name of the link used to reference the link regardless of its url domain
    path('store/', store, name="store"),
    
    path('store/<str:category_name>/', store, name="store"), #? comes after the fixed urls, allows to create multiple urls with varied names
    path('product/<int:product_id>/', view_product, name="view_product"),
    path('product/<int:product_id>/<int:id_color>/', view_product, name="view_product"),
    
    path('youraccount/', your_account, name="your_account"), 
    path('login/', login, name="login"), 
    path('cart/', cart, name="cart"), 
    path('checkout/', checkout, name="checkout"), 
    path('addtocart/<int:product_id>/', add_to_cart, name="add_to_cart"), 
]