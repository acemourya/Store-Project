from django.contrib import admin
from .models import User, Customer


# Register your models here.
class CustomerInline(admin.TabularInline):
    model = Customer


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    inlines = (CustomerInline, )
