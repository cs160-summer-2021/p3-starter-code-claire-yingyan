from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('home', views.home, name='home'),
    path('color_easy', views.color_easy, name='color_easy'),
    path('color_hard', views.color_hard, name='color_hard'),
    path('rec_easy', views.rec_easy, name='rec_easy'),
    path('rec_hard', views.rec_hard, name='rec_hard'),
    path('info', views.info, name='info')

]
