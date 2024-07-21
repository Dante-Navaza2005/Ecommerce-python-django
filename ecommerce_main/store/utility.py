from django.db.models import Max, Min


def filter_product(products, filter):
    if filter:
        if "-" in filter:
            category, product_type = filter.split("-")
            products = products.filter(category__slug = category, product_type__slug = product_type) 
            #? ABOVE gets the slug atribute from the category and product_type (in the database relationship it is described that way)class and filters it according to the name of the category obtained from the url
        else: #? client only filtered by the category
            products = products.filter(category__slug = filter) #? gets the slug atribute from the category class and filters it according to the name of the category obtained from the banner
    return products

def min_max_price (products) :
    min_price = 0
    max_price = 0

    if (len(products) > 0) : #? rounding function doesnt work for NaN values
        min_price = list(products.aggregate(Min("price")).values())[0] #? obtaining the maximum price (attribute from the Product class)
        max_price = list(products.aggregate(Max("price")).values())[0] #? obtaining the maximum price (attribute from the Product class)
        min_price = round(min_price, 2) #? rounding to two decimal places
        max_price = round(max_price, 2) #? rounding to two decimal places
    
    return min_price, max_price