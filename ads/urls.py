from django.urls import path, include, re_path

from . import views


urlpatterns = [
    path("", views.ListAdsView.as_view()),
    path("pending/", views.ListPendingAdsView.as_view()),
    path("rejected/", views.ListRejectedAdsView.as_view()),
    path("expired/", views.ListExpiredAdsView.as_view()),
    re_path(r"^moderate/(?P<pk>\d+)/$", views.StatusPartialUpdateView.as_view()),
    path("create/", views.CreateAdView.as_view()),
    path("my_ads/", views.MyAdsView.as_view()),
    path("sellers/",views.ListSellersAdsView.as_view()),
    re_path(r"^my_ads/edit/(?P<pk>\d+)/$", views.AdDetailDeleteView.as_view()),
    re_path(r"^(?P<pk>\d+)/$", views.AdDetailView.as_view()),
    path('top/',views.TopAdDetailView.as_view()),
]
