from django.urls import path 
from .views import * 
urlpatterns = [
    path('', indexview , name='indexview'),
    path('loginpage', loginview , name='loginview'),
    path('logoutview', logoutview , name='logoutview')
]
