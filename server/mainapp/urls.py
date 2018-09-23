from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page),
    path('catalog/', views.catalog_list),
    path('product/', views.product_detail),
]