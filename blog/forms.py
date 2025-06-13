from django import forms
from django.core.exceptions import ValidationError
import re
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValidationError("Name should contain only letters and spaces.")
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not re.match(r'^[\w\s\-\.\,\!\?]{3,100}$', subject):
            raise ValidationError("Subject can include letters, numbers, and punctuation (3-100 characters).")
        return subject

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Django already validates EmailField, but you can enforce stricter rules:
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValidationError("Enter a valid email address.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message.strip()) < 10:
            raise ValidationError("Message must be at least 10 characters long.")
        return message