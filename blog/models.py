from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='media', null=True, blank=True)
    card_head = models.CharField(max_length=100,null=True, blank=True)
    modal_head = models.CharField(max_length=100,null=True, blank=True)
    date = models.DateField()
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

    def __str__(self):
        return self.name
    

