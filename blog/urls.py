from django.urls import path
from django.urls import re_path
from . import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap(),
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', views.home, name='home'),
    path('*', views.home, name='home'),
    path('base', views.base, name='base'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('blog', views.blog_list, name='blog'),
    path('dashboard/', views.admin_panel, name='dashboard'),
    path('privacy_nmeapp', views.privacy, name='privacy_nmeapp'),
    path('blog_post', views.blog_post, name='blog_post'),
    path('update_blog', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
    path('delete_message/<int:id>', views.delete_message, name='delete_message'),
    # path('sitemap', views.sitemap, name='sitemap'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'), 
    # path('admin_register/', views.admin_register, name='admin_register'),

    re_path(r'^.*$', views.home, name='catch_all'),

]
