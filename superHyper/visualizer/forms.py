from django import forms

# from .models import 
from .models import URL 

class urlForm(forms.ModelForm):
    class Meta:
        model = URL 
        fields = [
        "link",
        ]