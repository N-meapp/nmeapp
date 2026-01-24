from django.contrib import admin
from .models import*
from django import forms


# Register your models here.
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(TeamMember)
admin.site.register(Testimonial)

