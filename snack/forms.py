from django import forms
from snack.models import Snacks

class SnackForm(forms.ModelForm):

    class Meta:
        model = Snacks
        fields = '__all__'
