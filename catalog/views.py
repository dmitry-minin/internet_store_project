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
