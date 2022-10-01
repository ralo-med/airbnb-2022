from django.contrib import admin
from .models import House

# Register your models here.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    list_display = (
        "name", "price","address", "pet_friendly"
    )
    list_filter = ("price","pet_friendly")
    search_fields= ("address",)