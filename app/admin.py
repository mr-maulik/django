from django.contrib import admin
from .models import ProductMst, ProductSubCat

# Register your models here.
admin.site.register(ProductMst)
admin.site.register(ProductSubCat)