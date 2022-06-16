from django.urls import path
from .import views

urlpatterns=[
    path('rl/',views.Register.as_view(),name='register.urls'),
    path('log/',views.Login.as_view(),name='login.urls'),
    path('lo/',views.Logout.as_view(),name='logout.urls'),
    path('otp/',views.VerifyOTPview.as_view(),name='otp.urls')
    

]