from django.urls import path, include, re_path

from . import views


urlpatterns = [
    path("", views.ListMyCars.as_view()),
    path("newcar/", views.CreateCar.as_view()),
    #re_path(r'^activate/(?P<pk>\d+)/$', views.StatusPartialUpdateView.as_view()),


]