from django import forms
from libraries.models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        exclude = ('book','user')
