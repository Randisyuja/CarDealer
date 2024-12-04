from django.urls import path, include
from CarDealer.categories import views


urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('<int:category_id>/', include([
        path('edit_category/', views.edit_category, name='edit_category'),
        path('delete_category/', views.delete_category, name='delete_category'),
    ]))
]
