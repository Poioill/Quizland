from django import forms
from django.forms import Textarea

from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_text',)
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['comment_text'].widget = Textarea(attrs={'rows':10})