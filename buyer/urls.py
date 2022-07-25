from django.urls import path
from . import views

urlpatterns = [
    path('', views.buyer_signup, name='buyer-signup'),
    path('byr-login', views.byr_login, name='byr-login'),
    path('buyer_verify', views.buyer_verify, name='buyer_verify'),
    path('byr-home', views.byr_home, name='byr-home'),
]

