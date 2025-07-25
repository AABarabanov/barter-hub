from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.AdListView.as_view(), name='ad_list'),
    path("create/", views.ad_create, name="ad_create"),
    path("<int:ad_id>/", views.ad_detail, name="ad_detail"),
    path("<int:ad_id>/proposal/", views.send_proposal, name="send_proposal"),
    path('login/',
     LoginView.as_view(template_name='ads/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
