from django.shortcuts import render, redirect
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, CategoryForm


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'

class ProductEditListView(ListView):
    model = Product
    template_name = 'edit_product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Сортируем продукты по категории
        return Product.objects.all().order_by('category')


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_edit')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:home')


class CategoryCreateView(CreateView):
    model = Product
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('catalog:product_edit')


class ContactTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        return render(request, 'confirm.html', {'name': name})