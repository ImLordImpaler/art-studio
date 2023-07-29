from django.urls import path 
from .views import * 


urlpatterns = [
    path('admin-page', admin_page , name='admin_page'),
    path('add-post', add_post , name='add_post'),
    path('add_post_type', add_post_type , name='add_post_type'),
    path('delete_post_type/<str:pk>', delete_post_type , name='delete_post_type'),
    path('delete_post/<str:pk>', delete_post , name='delete_post')
]
