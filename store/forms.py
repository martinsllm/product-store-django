from django import forms
from store.models import Category


class UploadFileForm(forms.Form):
    file = forms.FileField()
    name = forms.CharField(max_length=50)
    category = forms.ChoiceField(
        choices=[(category.id, category.title) for category in Category.objects.all()])
    quantity = forms.IntegerField()
    buy_price = forms.FloatField()
    sale_price = forms.FloatField()
