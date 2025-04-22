from django.urls import path

from items import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]