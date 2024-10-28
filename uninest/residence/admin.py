from django.contrib import admin
from .models import Building, Room

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'floor', 'building')
    list_filter = ('floor', 'building')
    search_fields = ('room_number',)
