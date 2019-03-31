from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Benutzername", max_length=30, required=True, help_text='')
    email = forms.EmailField(label="E-Mail Adresse (optional)", max_length=254, required=False, help_text='Aktuell wird die E-Mail Adresse nicht genutzt. Möglicherweise wird diese Adresse in Zukunft irgendwann für einen Newsletter oder eine tägliche / wöchentliche Zusammenfassung genutzt.')
    password1 = PasswordField(label="Passwort", max_length=150, required=True, help_text='')
    password2 = PasswordField(label="Passwort wiederholen", max_length=150, required=True, help_text='')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email' )
