from django import forms

from . models import Profile, Blog, Article

class ProfPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image_link',)
        widgets = {
            'image_link': forms.TextInput(attrs={'class': 'form-control col'})
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'body': forms.Textarea(attrs={'class': 'form-control col-md-8', 'style': 'margin: 0 auto'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'body': forms.Textarea(attrs={'class': 'form-control col-md-8', 'style': 'margin: 0 auto'}),
        }