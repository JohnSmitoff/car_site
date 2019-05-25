from django.urls import path, include, re_path

from . import views


urlpatterns = [
    path("", views.ListAds.as_view()),
    path("pending/", views.ListPendingAds.as_view()),
    path("rejected/", views.ListRejectedAds.as_view()),
    path("expired/", views.ListExpiredAds.as_view()),
    re_path(r"^moderate/(?P<pk>\d+)/$", views.StatusPartialUpdateView.as_view()),
    path("create/", views.CreateAd.as_view()),
    path("my_ads/", views.MyAds.as_view()),
    re_path(r"^my_ads/delete/(?P<pk>\d+)/$", views.AdDetailDelete.as_view()),

]
