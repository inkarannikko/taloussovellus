from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('', views.talous, name='talous'),
    path('upload/', views.upload, name='upload'),
    path('menot/', views.expenses, name='menot'),
    path('tulot/', views.incomes, name='tulot'),
    path('sijoitukset/', views.sijoitukset, name='sijoitukset'),
    path('kassavirta/', views.kassavirta, name='kassavirta'),
    path('paavalikko/',views.paavalikko, name='paavalikko')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
