from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=150)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(
        blank=False, null=False, default=0)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()

    def __str__(self):
        return self.nome


class Image(models.Model):
    image = models.ImageField(upload_to="imgs")
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
