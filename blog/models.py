from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    image = CloudinaryField('image', folder="nmeapp_blogs/",blank=True, null=True) 
    card_head = models.CharField(max_length=100,null=True, blank=True)
    modal_head = models.CharField(max_length=100,null=True, blank=True)
    date = models.CharField(max_length=100,null=True, blank=True)
    card_paragraph = models.TextField(null=True, blank=True)
    modal_paragraph = models.TextField(null=True, blank=True)
    keyword = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.keyword
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # plain text
    rate_limit = models.IntegerField(default=0)
    last_failed_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = CloudinaryField('image', folder="nmeapp_members/", blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonials/")
    rating = models.PositiveSmallIntegerField(default=5)  # 1-5
    opinion = models.TextField()

    def __str__(self):
        return self.name