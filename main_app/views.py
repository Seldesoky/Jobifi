from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile, JobPosting, Application
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import ApplicationForm


# Create your views Below.

def home(request):
    return render(request, 'home.html')

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

# apply_for_job

@login_required
def apply_for_job(request, id):
    job = get_object_or_404(JobPosting, id=id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.job_posting = job
            application.save()
            return redirect('job_detail', id=job.id)
    else:
        form = ApplicationForm()
    return render(request, 'apply_for_job.html', {'form': form, 'job': job})

#list job_applications

from django.contrib.auth.decorators import login_required

@login_required
def job_applications(request, id):
    job = get_object_or_404(JobPosting, id=id)
    if job.posted_by != request.user:
        return redirect('job_list') 
    applications = Application.objects.filter(job_posting=job)
    return render(request, 'job_applications.html', {'job': job, 'applications': applications})

# application_detail by id

@login_required
def application_detail(request, id):
    application = get_object_or_404(Application, id=id)
    if application.applicant != request.user and application.job_posting.posted_by != request.user:
        return redirect('job_list') 
    return render(request, 'application_detail.html', {'application': application})
