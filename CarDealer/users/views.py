from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from CarDealer.users.forms import SignUpForm, LoginForm


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
