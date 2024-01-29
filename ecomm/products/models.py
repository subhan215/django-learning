from django.db import models
from base.models import BaseModel
# Create your models here.


class Category(BaseModel) : 
      category_name = models.CharField(max_length=100)
      category_image = models.FileField(upload_to="categories")
      slug = models.SlugField(unique = True , null = True , blank = True)

class Product(BaseModel) : 
      product_name = models.CharField(max_length=100)
      category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name = "products")
      price = models.IntegerField()
      product_description = models.TextField()
      slug = models.SlugField(unique = True , null = True , blank = True)

class ProductImage(BaseModel) :
      product = models.ForeignKey(Product , on_delete = models.CASCADE , related_name = "product_image")
      image = models.FileField("product")      