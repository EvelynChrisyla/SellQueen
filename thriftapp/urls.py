from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landingPage, name="landing"),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('display', views.display_page, name="display"),
    path('create', views.create_product, name='create'),
    # path('test', views.image_request, name='image')
    path('payment', views.display_payment, name="payment"),
    path('detail/<int:id>', views.detail_product, name='detail'),
    path('profile', views.display_profile, name="profile")
]
