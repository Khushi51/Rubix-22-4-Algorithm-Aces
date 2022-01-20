import imp
from django import forms


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User

from appointment.models import Patient



class ProfileForm(forms.ModelForm):
     class Meta:
          model=Patient
          fields='__all__'

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs = {'class': 'form-control'}))

    password2 = forms.CharField(label="Password Again", widget=forms.PasswordInput(attrs = {'class': 'form-control'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    city = forms.CharField()
    phone = forms.CharField(max_length=20)



   
    class Meta:
        model = User
        fields = {'email','username','password1','password2'}
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus': True,'class': 'form-control'}))
    password = forms.CharField(
        label= "Password",
        strip = False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'})
    )
    email= forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

       