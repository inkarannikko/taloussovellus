from django.urls import path
from django.conf.urls import url
from.import views


urlpatterns = [
    path('', views.talous, name='talous'),
    path('upload/', views.upload, name='upload'),
    path('menot/', views.menot, name='menot'),
    path('tulot/', views.tulot, name='tulot'),
    path('sijoitukset/', views.sijoitukset, name='sijoitukset'),
    path('kassavirta/', views.kassavirta, name='kassavirta')
    
]
