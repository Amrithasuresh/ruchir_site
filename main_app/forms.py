from django import forms
from main_app import models

class ContactForm(forms.ModelForm):

    class Meta:
        model = models.ContactFormResponses
        fields = '__all__'
        
