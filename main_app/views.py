from django.shortcuts import render
from .models import Company
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views Below.

def home(request):
    return render(request, 'home.html')


def company_page(request):
    

    return render(request, 'company/detail.html',)
#Authentication / Creation of Users

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        phone_number = request.POST.get("phone_number")
        bio = request.POST.get("bio")
        role = request.POST.get("role")

        # Password check
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register_user")

        # If there is already an existing account
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already in use.")
            return redirect("register_user")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("register_user")
        
        # Create User
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(
                user=user,
                phone_number=phone_number,
                bio=bio,
                role=role,
            )
            login(request, user)
            messages.success(request, "User has been created successfully.")
            return redirect("home")
        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return redirect("register_user")
    
    # Render registration form
    return render(request, 'accounts/register.html')
# Change Django registration to custom template "accounts"
class CustomLoginView(LoginView):

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')   
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

# Login_Required

def job_seeker_profile(request):
    return render(request, 'profile/job_seeker.html')

def employer_profile(request):
    return(request, 'profile/empolyer.html')



class CompanyCreate(CreateView):
    model = Company
    fields = '__all__'
    success_url = '/companies/'

class CompanyUpdate(UpdateView):
    model = Company
    fields = '__all__'

class CompanyDelete(DeleteView):
    model = Company
    success_url = '/companies/'
