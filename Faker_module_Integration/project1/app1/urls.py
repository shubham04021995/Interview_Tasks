from django.urls import path
from .import views


urlpatterns=[
    path('se/',views.showemp,name='show.urls')
]