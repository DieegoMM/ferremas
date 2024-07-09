#from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('contacto',views.contacto, name='contacto'),
    path('registrar',views.registrar, name='registrar'),
    path('crud',views.crud, name='crud'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('BrowniesTodos', views.BrowniesTodos, name='BrowniesTodos'),
    path('browniesadd', views.browniesadd, name='browniesadd'),
    path('brownies_del',views.brownies_del, name='brownies_del'),
    path('brownies_findEdit',views.brownies_findEdit, name='brownies_findEdit')

]