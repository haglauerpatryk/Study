from django.shortcuts import render
from .models import Contact, Product
from django.contrib import messages
from math import ceil

# Create your views here.

def index(request):
    product_list = []
    product_dict = Product.objects.values('product_category', 'product_id')
    print(product_dict)
    cats = {item['product_category'] for item in product_dict}
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        product_list.append([prod, range(1, nSlides), nSlides])

    params = {'products_list': product_list}

    return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        desc  = request.POST.get('desc')
        pnumber = request.POST.get('pnumber')
        myquery = Contact(name=name, email=email, desc=desc, phonenumber=pnumber)
        myquery.save()
        messages.info(request, 'Your message has been sent successfully!')
        return render(request, 'contact.html')

    return render(request, 'contact.html')
