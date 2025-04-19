from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        blank=False, null=False, default=0)
    buy_price = models.FloatField()
    sale_price = models.FloatField()

    def __str__(self):
        return self.name


class File(models.Model):
    image = models.ImageField(upload_to="img")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
