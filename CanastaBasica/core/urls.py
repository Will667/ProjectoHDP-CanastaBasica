from django.urls import path
from.import views
from core.views import *



urlpatterns = [

    #Paths del core
    path('', views.home, name="home"),
    path('login', views.login, name="login"), #login
    path('test', views.test, name="test"), #depurar
    path('graficas', views.graficas, name="graficas"),
    path('tablas', views.tablas, name="tablas"),
    path('lista', views.test_view, name="lista"),
    
    path('testlist', test_list, name='test_list'),
    path('list', test_view, name='test_view'),
]