from django.contrib import admin
from .models.product import Product
from .models.categorty import Category
from .models.customer import Customer
from .models.order import Order
from .models.contactus import Contactus
from .models.feedback import Feedback


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Contactus)
admin.site.register(Feedback)



