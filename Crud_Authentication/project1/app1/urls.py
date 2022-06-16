from django.urls import path
from .import views


urlpatterns=[
    path('lv/',views.lapview,name='lapview.urls'),
    path('sl/',views.showlaptop,name='show.urls'),
    path('ul/<int:laptop_id>/',views.updatelaptop,name='update.urls'),
    path('dl/<laptop_id>/',views.deletelaptop,name='delete.urls')

]