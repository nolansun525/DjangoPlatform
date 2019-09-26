from django.contrib import admin

# Register your models here.
from .models import NewTable
from .models import Product

admin.site.register(NewTable)
admin.site.register(Product)