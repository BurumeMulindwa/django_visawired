from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('prices/index/', views.index),
    path('services/index/', views.index),
    path('prices/contact/', views.index),
    path('prices/about/', views.index),
    path('prices/pay_fast/', views.index),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('prices/', views.prices, name='prices'),
    path('contact/', views.contact, name='contact'),
    path('contact_captcha/', views.contact_captcha, name='contact_captcha'),
    path('pay_fast/', views.pay_fast, name='pay_fast'),
    path('contact/index/', views.contact, name='contact'),
    path('contact_landing/', views.contact_landing, name='contact_landing'),
]
