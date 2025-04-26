from django.shortcuts import render, redirect
from catalog.models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


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
