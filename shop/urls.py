from django.urls import path
from . import views
from .views import search, index

app_name = 'shop'

urlpatterns = [
    path('search/', search, name='search'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('filter/price/', views.filter_by_price, name='filter_by_price'),
]
