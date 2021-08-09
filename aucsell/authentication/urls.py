from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.authlogin,name='login'),
    path('registration/',views.authregistration,name='registration'),
    path('forgot-password/',views.authforgotpassword,name='forgotpassword'),
    path('logout/',views.logout,name='logout'),
]
