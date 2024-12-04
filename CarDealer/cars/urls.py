from django.urls import path, include
from CarDealer.cars import views


urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('add_car/', views.add_car, name='add_car'),
    path('<int:car_id>/', include([
        path('edit_car/', views.edit_car, name='edit_car'),
        path('delete_car/', views.delete_car, name='delete_car'),
    ]))

]
