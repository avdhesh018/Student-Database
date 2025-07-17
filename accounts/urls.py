from django.urls import path
from . import views
urlpatterns = [
    path('signuaccount/',views.signupaccount,name = 'signupaccount'),
    path('logoutaccount/',views.logoutaccount,name = 'logoutaccount'),
    path('loginaccount/',views.loginaccount,name = 'loginaccount'),
]