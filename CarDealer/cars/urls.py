from django.urls import path, include
from CarDealer.cars import views


urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('add_car/', views.add_car, name='add_car'),
    path('<int:car_id>/', include([
        path('car_detail/', views.car_detail, name='car_detail'),
        path('book_test_drive/', views.book_test_drive, name='test_drive'),
        path('edit_car/', views.edit_car, name='edit_car'),
        path('delete_car/', views.delete_car, name='delete_car'),
    ])),
    path('test_drive_user/', views.test_drive_user, name='test_drive_user'),
    path('test_drive_list/', views.test_drive_list, name='test_drive_list'),    
    path('test_drive_history_user/', views.test_drive_history_user, name='test_drive_history_user'),
    path('test_drive_history/', views.test_drive_history, name='test_drive_history'),
    path('<int:test_drive_id>/', include([
        path('edit_test_drive_status/', views.edit_test_drive_status, name='edit_test_drive_status'),
        path('delete_test_drive/', views.delete_test_drive, name='delete_test_drive'),
        path('cancel_test_drive/', views.cancel_test_drive, name='cancel_test_drive'),
    ]))

]
