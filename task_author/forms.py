from django import forms
from .models import Author

class PersonForm(forms.ModelForm):
    class Meta:  
        model = Author
        fields = '__all__'
