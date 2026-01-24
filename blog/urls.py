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
    path("contact-submit/", views.contact_submit, name="contact_submit"),
    path('dashboard/', views.admin_panel, name='dashboard'),
path("enquiry/delete/<int:id>/", views.delete_enquiry, name="delete_enquiry"),
path("team/add/", views.add_team_member, name="add_team_member"),
    path("team/update/<int:id>/", views.update_team_member, name="update_team_member"),
    path("team/delete/<int:id>/", views.delete_team_member, name="delete_team_member"),
    path('faq', views.faq, name='faq'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/edit/', views.edit_testimonial, name='edit_testimonial'),
    path('testimonials/delete/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
    path('privacy_nmeapp', views.privacy, name='privacy_nmeapp'),
    path('blog_post', views.blog_post, name='blog_post'),
    path('update_blog', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
    path('delete_message/<int:id>', views.delete_message, name='delete_message'),
    # path('sitemap', views.sitemap, name='sitemap'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'), 
    # path('admin_register/', views.admin_register, name='admin_register'),

    # re_path(r'^.*$', views.home, name='catch_all'),

]
