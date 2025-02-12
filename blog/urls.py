from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('blog', views.blog_list, name='blog'),

    # path('about/', views.about, name='about'),
]