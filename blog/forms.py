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
        if not re.match(r'^[A-Za-z\s]{5,}$', name):
            raise ValidationError("Name must be at least 5 characters long and contain only letters and spaces.")
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not re.match(r'^[A-Za-z0-9\s\.\-]{3,100}$', subject):
            raise ValidationError("Subject can only include letters, numbers, spaces, dots, and hyphens (3–100 chars).")
        return subject

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[\w\.-]+@gmail\.com$', email):
            raise ValidationError("Only Gmail addresses ending with @gmail.com are allowed.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message.strip()) < 10:
            raise ValidationError("Message must be at least 10 characters long.")
        if not re.match(r'^[A-Za-z0-9\s\.\-]+$', message):
            raise ValidationError("Message can only include letters, numbers, spaces, dots, and hyphens.")
        return message