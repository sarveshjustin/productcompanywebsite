from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def products(request):
    return render(request,"products.html")

def people(request):
    return render(request,"people.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

