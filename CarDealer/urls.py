"""
URL configuration for CarDealer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from CarDealer.users import views as vu
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vu.homepage, name='home'),
    path('about/', vu.about, name='about'),
    path('users/', include('CarDealer.users.urls')),
    path('cars/', include('CarDealer.cars.urls')),
    path('categories/', include('CarDealer.categories.urls')),
    path('locations/', include('CarDealer.locations.urls')),
    path('brands/', include('CarDealer.brands.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
