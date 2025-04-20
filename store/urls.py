from django.urls import path
from store.views.ProductListView import ProductListView
from store.views.ProductUpdateView import ProductUpdateView
from store.views.ProductCreateView import ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<slug:slug>', ProductUpdateView.as_view(), name='product_update'),
]
