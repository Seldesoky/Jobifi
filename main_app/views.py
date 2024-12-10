from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import UserProfile
# Create your views here.

def home(request):
    return render(request, 'home.html')

#Authentication / Creation of Users
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        phone_number = request.POST.get('phone_number')
        bio = request.POST.get('bio')
        role = request.POST.get('role')

    #Password
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register_user")

    #Check for accounts already in use
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already in use.")
            return redirect("register_user")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("register_user")
    
    # try to create user and profile
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = UserProfile.objects.create(
            user=user,
            phone_number=phone_number,
            bio=bio,
            role=role,
        )
        login(request, user)
        messages.success(request, "User has been created")
        return redirect("home")
    except Exception as e:
        messages.error(request, f"Error creating a user: {e}")
        return redirect("register_user")
    
    return render(request, "register.html")
