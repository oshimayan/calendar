from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/api/', views.api, name='api'),
    path('ajax/api_delete/', views.api_delete, name='api_delete')
]
