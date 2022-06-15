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
]
