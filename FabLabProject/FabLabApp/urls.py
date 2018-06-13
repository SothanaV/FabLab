from django.urls import path
from .views import*
urlpatterns =[
    path('',home,name='home'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    path('elements/',elements,name='elements'),
    path('services/',services,name='services'),
]