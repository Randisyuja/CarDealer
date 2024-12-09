from django.urls import path, include
from CarDealer.brands import views

urlpatterns = [
    path('', views.BrandList.as_view(), name='brands_list'),
    path('add_brand/', views.AddBrand.as_view(), name='add_brand'),
    path('<int:brand_id>/', include([
        path('edit_brand/', views.EditBrand.as_view(), name='edit_brand'),
        path('delete_brand/', views.DeleteBrand.as_view(), name='delete_brand'),
    ]))
]
