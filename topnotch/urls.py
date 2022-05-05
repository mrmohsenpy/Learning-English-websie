from django.urls import path
from . import views 

urlpatterns =[
    path('', views.topnotch ,name='topnotch'),
    path('vocabulary', views.vocabulary , name='vocabulary'),
    path('grammer' , views.grammer , name='grammer'),
    path('blog' , views.blog , name='blog'),
    path('speaking' , views.speaking , name='speaking'),
    path('shop' , views.shop , name='shop'),
    path('sentences' , views.sentences , name='sentences'),
    path('home' , views.home , name='home'),
    # path('course' , views.course , name='course'),


 
]