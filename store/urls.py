from django.urls import path
from . import views
urlpatterns = [
 path('', views.store, name="store"),
 path('cart/', views.cart, name="cart"),
 path('checkout/', views.checkout, name="checkout"),
 path('buscar/', views.get, name="buscar"),
 path('login/', views.login, name="login"),
 path('register/', views.register, name="register"),
 path('login/register.html',views.register)
]