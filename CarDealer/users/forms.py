from django import forms
from CarDealer.users.models import User


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Anda bisa menambahkan validasi password di sini
        return password


class UserRegistrationForm(UserBaseForm):
    pass


class UserEditForm(UserBaseForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Tambahkan validasi untuk email jika diperlukan
        return email


class UserDeleteForm(UserBaseForm):
    pass

