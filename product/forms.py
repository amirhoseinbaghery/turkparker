from django import forms
from django.forms import Textarea
from blog.models import BlogComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('body',)
        widgets = {
            'body': Textarea(
                attrs={'cols': 40, 'rows': 6,
                       'class': 'form-control form-control-solid placeholder-gray-600 fw-bolder fs-4 ps-9 pt-7',
                       'placeholder': 'دیدگاه خود را بنویسید'}),
        }
        labels = {
            'body': ''
        }
