from django.shortcuts import render, redirect

from catalog.models import Product


def home(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(request, 'products_list.html', context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        return render(request, 'confirm.html', {'name': name})
    return render(request, 'contacts.html')


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context=context)
