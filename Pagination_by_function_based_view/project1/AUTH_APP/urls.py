from django.urls import path
from .import views

urlpatterns=[
    path('reg/',views.registerview,name='register.urls'),
    path('log/',views.loginview,name='login.urls')
]