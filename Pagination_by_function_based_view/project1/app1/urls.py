from django.urls import path
from .import views

urlpatterns=[
    path('ev/',views.empview,name='emp.urls'),
    path('se/',views.showemp,name='show.urls'),
    path('uv/<int:eid>/',views.updateview,name='update.urls'),
    path('dv/<int:eid>/',views.deleteview,name='delete.urls')
]