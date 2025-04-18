from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from store.forms import UploadFileForm


class ProductCreateView(LoginRequiredMixin, View):
    def get(self, request):
        data = {'form': UploadFileForm()}
        return render(request, 'store/add_product.html', data)
