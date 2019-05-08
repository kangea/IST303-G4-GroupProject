from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Brand, Product, ProductURL, CustomUser, SavedProduct

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('discord',)}),)
    model = CustomUser
    list_display = ['email', 'username', 'discord']

class ProductURLInLine(admin.TabularInline):
    model = ProductURL
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','brand','SKU','instock','picture_url','price',
        'restock_date','original_release_date']
    inlines = [ProductURLInLine]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(SavedProduct)
