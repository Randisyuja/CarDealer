from django.contrib import admin
from CarDealer.categories.models import Category


class CategoriesAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']  # Menampilkan kolom di halaman daftar
    list_filter = ['name']  # Menambahkan filter di sisi kanan
    search_fields = ['name']  # Menambahkan kolom pencarian
    ordering = ['name']  # Mengatur urutan daftar


admin.site.register(Category, CategoriesAdmin)
