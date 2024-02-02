from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


def sign_up_user(request):
    if request.user.is_authenticated:
        return redirect(to="quotesapp:main")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "users/signup.html", context={"form": form})

    return render(request, "users/signup.html", context={"form": RegisterForm()})


def log_in_user(request):
    if request.user.is_authenticated:
        return redirect(to="quotesapp:main")

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotesapp:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})


@login_required
def log_out_user(request):
    logout(request)
    return redirect(to="quotesapp:main")
