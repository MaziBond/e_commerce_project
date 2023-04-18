from django.db import models
from user_auth.models import User
from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, null=True)
    brand_name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='products')
    product_release_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.product_name}'

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        return True

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
