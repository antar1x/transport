from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'phone', 'service', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше ім’я'}),
            'phone': forms.TextInput(attrs={'placeholder': '+38 (0__) ___-__-__'}),
            'service': forms.Select(),
            'comment': forms.Textarea(attrs={'placeholder': 'Коротко опишіть, що потрібно зробити', 'rows': 4}),
        }
