"""car_ads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path, path
from ads.views import BuildTriger
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("admin/", admin.site.urls),
    # re_path(r'^api/v1/sitemap/$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/ads/", include("ads.urls")),
    path("api/v1/my_cars/", include("cars.urls")),
    path("api/v1/ads/task/", BuildTriger.as_view()),
]
