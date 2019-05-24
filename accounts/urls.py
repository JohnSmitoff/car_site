from django.urls import path, include

from . import views


urlpatterns = [
    path("auth/", include("rest_auth.urls")),
    path("register/", views.SellerCreate.as_view(), name="register"),

]
