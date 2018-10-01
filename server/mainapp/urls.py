from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('catalog/', views.catalog_list, name='catalog'),
    path('<int:pk>/', views.product_detail, name='brooch'),
    path('contacts/', views.contacts, name='contacts'),
]
