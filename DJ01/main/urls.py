from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('base', views.base, name='base'),
    path('test', views.test, name='test'),

]
