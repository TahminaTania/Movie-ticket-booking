
from django import forms
# from .models import participant


class reg(forms.Form):
    email = forms.EmailField(label='your email')
    #  class Meta:
    #      model= participant
    #      fields=['email']
