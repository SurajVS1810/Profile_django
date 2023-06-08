from django.contrib import admin
from .models import home
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','education','skills','phone','github','email','linkedin','achievment')

admin.site.register(home)
