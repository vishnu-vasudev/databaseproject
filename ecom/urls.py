from django.urls import path

from data.views import loginfn
from . import views

urlpatterns = [
    path('',views.f1),
    path('seller', views.seller, name = 'seller-page'),
    path('seller-home', views.seller_home, name = 'seller-home'),
    path('seller-login', views.seller_login, name = 'seller-login'),
    path('pd-delete/<int:id>', views.pd_delete, name = 'pd-delete'),
    path('tempurl', views.tempurl, name = 'tempurl'),
    path('tempurl2', views.tempurl2, name = 'tempurl2'),
]