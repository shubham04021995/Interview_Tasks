from django import views
from django.urls import path
from .views import LaptopCreate, LaptopDetails, LaptopView, deleteView, updateView


urlpatterns=[
    path('lv/',LaptopCreate.as_view(),name='register.urls'),
    path('sv/',LaptopView.as_view(),name='show.urls'),
    path('ld/<int:pk>/',LaptopDetails.as_view(),name='single.urls'),
    path('uv/<int:pk>/',updateView.as_view(),name='update.urls'),
    path('dv/<int:pk>/',deleteView.as_view(),name='delete.urls')

]