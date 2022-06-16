from django.urls import path
from .import views

urlpatterns=[
    path('b1/',views.AddView.as_view(),name='addurl'),
    path('b2/',views.Showdata.as_view(),name='showurl'),
    path('b3/<int:id>/',views.ShowoneCus.as_view(),name='showoneurl'),
    path('b4/',views.ShowCus.as_view(),name='showurl1')
]