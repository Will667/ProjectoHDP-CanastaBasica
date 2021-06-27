from django.urls import path
from.import views
from core.views import encuesta_list



urlpatterns = [

    #Paths del core
    path('', views.home, name="home"),
    path('login', views.login, name="login"), #login
    path('test', views.test, name="test"), #depurar
    path('graficas', views.graficas, name="graficas"),
    path('tablas', views.tablas, name="tablas"),
    path('edicion', views.edicion, name="edicion"),
    # path('base', views.base, name="base"),

    path('list', encuesta_list, name='encuesta_list'),
]