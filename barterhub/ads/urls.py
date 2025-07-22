from django.urls import path
from . import views


urlpatterns = [
    path("", views.ad_list, name="ad_list"),
    path("create/", views.ad_create, name="ad_create"),
    path("<int:ad_id>/", views.ad_detail, name="ad_detail"),
    path("<int:ad_id>/proposal/", views.send_proposal, name="send_proposal"),
]
