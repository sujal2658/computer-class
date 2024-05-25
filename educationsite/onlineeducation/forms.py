from .models import feedbackModel
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Textarea

class feedbackForm(ModelForm):
    class Meta:
        model = feedbackModel
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter your name', 'class': 'box', 'maxlength': '50'}),
            'email': EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'box', 'maxlength': '250'}),
            'number': NumberInput(attrs={'placeholder': 'Enter your number', 'class': 'box'}),
            'message': Textarea(attrs={'placeholder': 'Enter your message', 'class': 'box', 'required': True, 'maxlength': '1000', 'cols': '30', 'rows': '10'}),
        }