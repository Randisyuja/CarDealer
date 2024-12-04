from django.urls import path, include
from CarDealer.brands import views

urlpatterns = [
    path('', views.brands_list, name='brands_list'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('<int:brand_id>/', include([
        path('edit_brand/', views.edit_brand, name='edit_brand'),
        path('delete_brand/', views.delete_brand, name='delete_brand'),
    ]))
]
