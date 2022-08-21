from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.productpage, name='product'),
    path('category/<str:category>', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('cart/', views.Cart, name='Cart'),

]