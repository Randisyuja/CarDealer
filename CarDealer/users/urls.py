from django.urls import path, include
from CarDealer.users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('<int:user_id>/', include([
        path('edit_user/', views.edit_user, name='edit_user'),
        path('delete_user/', views.delete_user, name='delete_user'),
    ])),
    path('users_list/', views.user_list, name='user_list')
]
