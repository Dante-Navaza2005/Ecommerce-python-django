from .models import Order, OrderedItem

def cart(request) :
    product_amount_cart = 0
    if request.user.is_authenticated:
        client = request.user.client #? one to one relationship
    else :
        return {"product_amount_cart" : product_amount_cart}
    order, created = Order.objects.get_or_create(client=client, finished=False) #? will get or create a new order if there is none for the client mentioned above. Will return the order and a boolean that says if it was created or not
    #! How many products are on the user's order
    items_ordered = OrderedItem.objects.filter(order = order) #? gets all the items of the order
    for item in items_ordered:
        product_amount_cart += item.quantity #? adds the quantity of each item as one order can have many items
    return {"product_amount_cart" : product_amount_cart, "items_ordered" : items_ordered}