from django.contrib import admin

from .models import Product,ProductUser
# Register your models here.
admin.site.register(ProductUser)
admin.site.register(Product)
