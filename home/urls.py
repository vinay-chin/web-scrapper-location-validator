from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home),
    path('scrap', views.scrap),
    path('validate', views.validate),
    path('results', views.results),
]