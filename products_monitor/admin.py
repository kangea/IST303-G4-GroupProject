from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Brand, Product, CustomUser, SavedProduct, ProductKeyWord

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('discord',)}),)
    model = CustomUser
    list_display = ['email', 'username', 'discord']

class ProductKeyWordInLine(admin.TabularInline):
    model = ProductKeyWord
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','brand','SKU','instock','picture_url','price','original_release_date','discordChannelLink','channelWebhook']
    inlines = [ProductKeyWordInLine]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(SavedProduct)
