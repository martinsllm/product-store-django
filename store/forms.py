from django import forms
from store.models import Category


class UploadFileForm(forms.Form):
    file = forms.FileField()
    nome = forms.CharField(max_length=50)
    categoria = forms.ChoiceField(
        choices=[(category.id, category.title) for category in Category.objects.all()])
    quantidade = forms.IntegerField()
    preco_compra = forms.FloatField()
    preco_venda = forms.FloatField()
