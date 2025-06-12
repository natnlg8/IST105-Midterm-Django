from email.policy import default

from django import forms


class MathForm(forms.Form):
    number1 = forms.DecimalField(label='Enter a number 1', required=True, decimal_places=2)
    number2 = forms.DecimalField(label='Enter a number 2', required=True, decimal_places=2)
    operator = forms.ChoiceField(choices=[('+', 'Addition'),('-', 'Substraction'), ('*', 'Multiply'), ('/', 'Division')], required=True, label='Select an operation')
