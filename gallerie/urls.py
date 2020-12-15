from django.urls import path
from . import views

app_name = 'gallerie'

urlpatterns = [
    path('', views.all_galleries, name='all_galleries'),
    path('', views.all_galleries, name='all_galleries'),
]