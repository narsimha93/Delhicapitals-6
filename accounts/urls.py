from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
#api url
    path('registerapi/', views.Registerapi.as_view(),name="register"),
    path('loginapi/', views.Loginapi.as_view()),
]
