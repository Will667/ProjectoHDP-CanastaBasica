from django.urls import path
from.import views

urlpatterns = [

    #Paths del core
    path('', views.home, name="home"),
    path('login', views.login, name="login"), #login
    path('test', views.test, name="test"), #depurar
    path('graficas', views.graficas, name="graficas"),
    path('tablas', views.tablas, name="tablas"),
    # path('base', views.base, name="base"),

]