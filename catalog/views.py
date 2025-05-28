from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, CategoryForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'

class ProductEditListView(LoginRequiredMixin, ListView):
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_edit')

    def get_form_class(self):
        if self.request.user.has_perm('catalog.add_product'):
            return ProductForm
        return PermissionDenied

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

    def get_form_class(self):
        self.object = self.get_object()
        if self.request.user == self.object.owner:
            return ProductForm
        elif self.request.user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        return PermissionDenied

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user == self.object.owner:
            return super().get(request, *args, **kwargs)
        elif request.user.has_perm('catalog.delete_product'):
            return super().get(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to delete this product.")

    def get_success_url(self):
        return reverse('catalog:home')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('catalog:product_edit')


class ContactTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        return render(request, 'confirm.html', {'name': name})
