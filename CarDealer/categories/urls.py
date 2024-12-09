from django.urls import path, include
from CarDealer.categories import views


urlpatterns = [
    path('', views.CategoryList.as_view(), name='category_list'),
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('<int:category_id>/', include([
        path('edit_category/', views.EditCategory.as_view(), name='edit_category'),
        path('delete_category/', views.DeleteCategory.as_view(), name='delete_category'),
    ]))
]
