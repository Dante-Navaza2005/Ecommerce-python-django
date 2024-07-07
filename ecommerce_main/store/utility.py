
def filter_product(products, filter):
    if filter:
        if "-" in filter:
            category, product_type = filter.split("-")
            products = products.filter(category__slug = category, product_type__slug = product_type) 
            #? ABOVE gets the slug atribute from the category and product_type (in the database relationship it is described that way)class and filters it according to the name of the category obtained from the url
        else: #? client only filtered by the category
            products = products.filter(category__slug = filter) #? gets the slug atribute from the category class and filters it according to the name of the category obtained from the banner
    return products