from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('home', views.home, name='home'),
    path('color_relaxed', views.color_relaxed, name='color_relaxed'),
    path('color_creative', views.color_creative, name='color_creative'),
    path('rec_easy', views.rec_easy, name='rec_easy'),
    path('rec_creative', views.rec_hard, name='rec_creative'),
    path('info', views.info, name='info')

]
