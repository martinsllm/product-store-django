from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get(self, request):
        products = Product.objects.all()
        data = {'products': products}
        return render(request, 'store/product_list.html', data)
