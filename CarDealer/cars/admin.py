from django.contrib import admin
from CarDealer.cars.models import Cars


class CarsAdmin(admin.ModelAdmin):
    fields = ('car_image', 'cars_name', 'brand', 'category', 'warna', 'tahun', 'CC', 'price', 'location', 'description')
    list_display = ('cars_name', 'brand', 'category', 'warna', 'tahun', 'CC', 'price', 'location', 'description')  # Menampilkan kolom di halaman daftar
    list_filter = ['cars_name', 'brand', 'category', 'location']  # Menambahkan filter di sisi kanan
    search_fields = ['cars_name']  # Menambahkan kolom pencarian
    ordering = ('cars_name',)  # Mengatur urutan daftar


admin.site.register(Cars, CarsAdmin)
