from django.contrib import admin
from .models import Court, Location

# Register your models here.

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('court_name', 'court_type','availability','location')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city','district')