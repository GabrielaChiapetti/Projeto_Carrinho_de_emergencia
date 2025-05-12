from django.urls import path

from item import views

app_name = 'item'

urlpatterns = [
    path('<int:item_id>/', views.item, name='item'), # página de cada ítem, criando nova url, sempre colocar barra final ao fim da url
    path('', views.index, name='index'),             # página inicial
    
]