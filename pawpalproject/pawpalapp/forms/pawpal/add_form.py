from django import forms
from ...models import PawPal

class AddPawPalForm(forms.ModelForm):

    class Meta:
        model = PawPal
        fields = ['name', 'birth_date', 'favorite_treat', 'favorite_toy']

