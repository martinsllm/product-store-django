from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Product
from store.forms import ProductForm


class ProductView(LoginRequiredMixin, View):
    model = Product

    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        data = product.__dict__
        data['category'] = product.category.id
        form = ProductForm(initial=data)
        return render(request, 'store/product.html', {'form': form, 'product': data})
