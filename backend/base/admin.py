from django.contrib import admin
from . import models
# Register your models here.

# @admin.register(models.Product)
# class ProductModelAdmin(admin.ModelAdmin):
#   pass

admin.site.register(models.Product)
admin.site.register(models.Review)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.ShippingAddress)
 