from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content','create_by','update_by')



# class SendEmail(forms.Form):
#     title = forms.CharField(max_length=200)
#     email = forms.EmailField()
#     content = forms.CharField(widget=forms.Textarea)
#     cc = forms.BooleanField()

class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc = forms.BooleanField()
