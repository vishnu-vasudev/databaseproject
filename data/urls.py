from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('department', views.dptfn, name='department'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('student', views.studentfn, name='student'),
    path('st_delete/<int:id>', views.st_delete, name='st_delete'),  
    path('login', views.loginfn, name='login'),
    path('home', views.homefn, name='home'),
    path('upd-password', views.password, name='upd-password'),
    path('img-display', views.imgdisplay, name='img-display'),
    path('insert', views.ajax, name='insert'),
    path('mailcheck', views.mailcheck, name='mailcheck'),
    path('ajax-display', views.ajax_display, name='ajax-display'),
    path('tempurl', views.tempurl, name='tempurl'),
    path('tempurl2', views.tempurl2, name='tempurl2'),
    path('tempurl3', views.tempurl3, name='tempurl3'),
    path('tempurl4', views.tableupdate, name='tempurl4'),
    path('staff', views.staff, name='staff'),
    path('staff-display', views.staff_display, name='staff-display'),
    path('test', views.index, name='test')
]
