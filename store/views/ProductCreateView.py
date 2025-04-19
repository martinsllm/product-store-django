from datetime import date
from io import BytesIO
import sys
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.mixins import LoginRequiredMixin
from store.forms import UploadFileForm
from store.models import Product, File


class ProductCreateView(LoginRequiredMixin, CreateView):
    def get(self, request):
        data = {'form': UploadFileForm()}
        return render(request, 'store/add_product.html', data)

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST.get('name')
            category = request.POST.get('category')
            quantity = request.POST.get('quantity')
            buy_price = request.POST.get('buy_price')
            sale_price = request.POST.get('sale_price')

            product = Product(name=name, category_id=category,
                              quantity=quantity, buy_price=buy_price, sale_price=sale_price)
            product.save()

            f = request.FILES.get('file')
            name = f'{date.today()}-{product.id}.jpg'

            img = Image.open(f)
            img = img.convert('RGB')
            img = img.resize((300, 300))
            output = BytesIO()
            img.save(output, format='JPEG', quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(
                output,
                'ImageField',
                name,
                'image/jpeg',
                sys.getsizeof(output),
                None
            )

            uploaded_file = File(image=img_final, product=product)
            uploaded_file.save()

            return redirect(reverse('index'))
