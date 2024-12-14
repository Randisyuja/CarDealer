from django.contrib import admin
from CarDealer.locations.models import Location


class LocationsAdmin(admin.ModelAdmin):
    fields = ['location']
    list_display = ['location']  # Menampilkan kolom di halaman daftar
    list_filter = ['location']  # Menambahkan filter di sisi kanan
    search_fields = ['location']  # Menambahkan kolom pencarian
    ordering = ['location']  # Mengatur urutan daftar


admin.site.register(Location, LocationsAdmin)
