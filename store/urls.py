from django.urls import path
from store.views.ProductListView import ProductListView
from store.views.ProductCreateView import ProductCreateView
from store.views.ProductUpdateView import ProductUpdateView
from store.views.ProductDeleteView import ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<slug:slug>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<slug:slug>',
         ProductDeleteView.as_view(), name='product_delete'),
]
