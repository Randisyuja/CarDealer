from django.contrib import admin
from CarDealer.brands.models import Brands


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_established', 'description')  # Menampilkan kolom di halaman daftar
    list_filter = ['name']  # Menambahkan filter di sisi kanan
    search_fields = ['name']  # Menambahkan kolom pencarian
    ordering = ('name',)  # Mengatur urutan daftar


admin.site.register(Brands, BrandsAdmin)
