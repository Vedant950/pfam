from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.aboutUs, name="about-us"),
    path('our-product/', views.ourProduct, name="our-product"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('scheduler/<str:pk>/', views.scheduler, name="scheduler"),
    path('status/<str:pk>/', views.status, name="status"),
    path('reset-password/', views.resetPassword, name="reset-password"),
    path('add-pet/<str:pk>/', views.addPet, name="add-pet")
]
