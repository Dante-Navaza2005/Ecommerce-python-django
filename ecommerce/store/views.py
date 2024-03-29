from django.shortcuts import render

# Create your views here.
def homepage(request): #? the first parameter always has to be a request
    return render(request, 'homepage.html') #? returns the homepage

