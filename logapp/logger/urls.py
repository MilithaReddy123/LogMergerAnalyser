from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('merge/', views.index, name='merge'),
    path('download_output/', views.download_file, name='download_file'),
    path('filter/', views.filter, name='filter'),
    path('search/', views.search, name='search'),
    path('view_log/', views.view_log, name='view_log'),
    path('view_support_bundle/', views.view_support_bundle, name='view_suppport_bundle'),
    path('generate_support_bundle/', views.generate_support_bundle, name='generate_support_bundle'),
    path("check_status/",views.check_service_status,name='check_service_status')
]