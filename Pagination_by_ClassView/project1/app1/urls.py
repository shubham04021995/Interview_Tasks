from django.urls import path
from .import views

urlpatterns=[
    path('al/',views.AddLap.as_view(),name='add.urls'),
    path('sl/',views.Showlap.as_view(),name='show.urls'),
    path('uv/<int:pk>/',views.Updatelap.as_view(),name='update.urls'),
    path('dv/<int:pk>/',views.Deletelap.as_view(),name='delete.urls')

]