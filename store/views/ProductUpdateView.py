from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Product
from store.forms import ProductForm


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy("product_list")

    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        data = product.__dict__
        data['category'] = product.category.id
        form = ProductForm(initial=data)
        return render(request, 'store/product.html', {'form': form, 'product': data})
