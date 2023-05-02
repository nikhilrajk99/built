from . import views
from django.urls import path
app_name='furnitureapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('shop',views.shop,name='shop')
]