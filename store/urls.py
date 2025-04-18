from django.urls import path
from store.views.ProductCreateView import ProductCreateView

urlpatterns = [
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
]
