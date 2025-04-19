from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        blank=False, null=False, default=0)
    buy_price = models.FloatField()
    sale_price = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class File(models.Model):
    image = models.ImageField(upload_to="img")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
