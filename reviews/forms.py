from django import forms
from .models import Review, Response


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment')
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your review here', 'rows': 8}),
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('comment')
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your response here', 'rows': 4}),
        }