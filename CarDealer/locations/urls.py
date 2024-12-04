from django.urls import path, include
from CarDealer.locations import views


urlpatterns = [
    path('', views.locations_list, name='locations_list'),
    path('add_location/', views.add_location, name='add_location'),
    path('<int:location_id>/', include([
        path('edit_location/', views.edit_location, name='edit_location'),
        path('delete_location/', views.delete_location, name='delete_location'),
    ]))
]
