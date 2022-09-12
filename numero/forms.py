from django import forms


class BirthdayForm(forms.Form):
    bday = forms.DateField(
        label="Дата рождения",
        initial='01.12.1990',
        required=True,
    )