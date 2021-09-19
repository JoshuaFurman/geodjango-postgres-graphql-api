from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Place

# Register your models here.
@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    list_display = (
        'title',
        'description',
        'coordinates',
    )
