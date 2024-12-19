from django import forms
from CarDealer.users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your Password',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your Password',
            'class': 'form-control'
        })
    )
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


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label="Your Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Pastikan menggunakan 'form-control'
            'placeholder': 'Enter your name',
        }))

    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',  # Pastikan menggunakan 'form-control'
            'placeholder': 'Enter your email',
        }))

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Pastikan menggunakan 'form-control'
            'placeholder': 'Enter your message',
        }), 
        label="Your Message"
        )

