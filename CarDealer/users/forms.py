from django import forms
from CarDealer.users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your Username', 'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email', 'class':'form-control'}),
        }
        help_texts = {
            'username': None,  # Menghapus help text
            'email': None,
            'password1': None,
            'password2': None,
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''  # Menghapus teks di password1
        self.fields['password2'].help_text = ''  # Menghapus teks di password2



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Pastikan menggunakan 'form-control'
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  # Pastikan menggunakan 'form-control'
            'placeholder': 'Enter your password',
        })
    )
