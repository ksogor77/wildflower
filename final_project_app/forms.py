from django import forms
# from django.forms.widgets import DateTimeInput

from . models import Profile

class ProfPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image_link',)
        widgets = {
            'image_link': forms.TextInput(attrs={'class': 'form-control col'})
        }