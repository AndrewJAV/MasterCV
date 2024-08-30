from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('person/<slug:slug>/', views.cv_detail, name='cv_view'),
    path('search/', views.search, name='search')
]
