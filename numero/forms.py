from django import forms
from datetime import datetime


class BirthdayForm(forms.Form):
    bday = forms.DateField(
        label="Дата рождения",
        required=True,
        widget=forms.TextInput(attrs={
            'pattern': '([0-9]{2}[.]{1}){2}[0-9]{4}',
            'placeholder': datetime.now().strftime("%d.%m.%Y"),
        })
    )