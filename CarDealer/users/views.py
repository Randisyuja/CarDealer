from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from CarDealer.users.forms import SignUpForm, LoginForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Ambil data dari form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Kirim email
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=f"Message:\n{message}\n\nFrom: {name} ({email})",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['randijordan8@gmail.com'],  # Email tujuan
                fail_silently=False,
            )
            # Kirim ke template untuk menampilkan popup sukses
            return render(request, 'users/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    
    return render(request, 'users/contact.html', {'form': form})



def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect ke homepage jika sudah login
        
    if request.method == 'POST':
        form = SignUpForm(request.POST)  # Correct usage
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect ke homepage jika sudah login

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Ganti dengan URL yang sesuai
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def homepage(request):
    return render(request, template_name='users/homepage.html')


def about(request):
    return render(request, template_name='about.html')
