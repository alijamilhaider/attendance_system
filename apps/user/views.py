from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model

from .forms import ImageForm

User = get_user_model()


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username, email = request.POST.get('username'), request.POST.get('email')
        pass1, pass2 = request.POST.get('password1'), request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        user = User.objects.create_user(username, email, pass1)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST.get('email')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_view(request):
    form = ImageForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            image_object = form.cleaned_data['image']
            request.user.profile_picture = image_object
            request.user.save()
        return redirect('/')
    user = request.user
    context = {"username": user.username, "profile_picture": user.profile_picture, "form": form}
    return render(request=request, template_name="home.html", context=context)
