from django.urls import path
from catalog.views import (ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
                           ContactTemplateView,ProductEditListView, CategoryCreateView, ProductListByCategoryView)


app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/edit/', ProductEditListView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/products/', ProductListByCategoryView.as_view(), name='products_in_category'),
]
