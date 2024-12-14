from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, JobPosting, Application
from .forms import JobPostingForm, ApplicationForm, UserProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views Below.

def home(request):
    return render(request, 'home.html')


def company_page(request):
    return render(request, 'company/detail.html',)


# Authentication / Creation of Users
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

        # Check for existing user
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already in use.")
            return redirect("register_user")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("register_user")
        
        # Create User and Profile
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


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')   


def logout_view(request):
    logout(request)
    return redirect('login')


# Job Views
def job_list(request):
    jobs = JobPosting.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(JobPosting, id=id)
    return render(request, 'jobs/job_detail.html', {'job': job})


# Profiles
@login_required
def job_seeker_profile(request):
    if request.user.profile.role != 'job_seeker':
        messages.error(request, "You do not have access to this page.")
        return redirect('home')
    return render(request, 'profile/job_seeker.html', {'profile': request.user.profile})


@login_required
def edit_job_seeker_profile(request):
    if request.user.profile.role != 'job_seeker':
        messages.error(request, "You do not have access to this page.")
        return redirect('home')
    
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('job_seeker_profile')
    else:
        form = UserProfileForm(instance=request.user.profile)

    return render(request, 'profile/edit_job_seeker.html', {'form': form})


@login_required
def employer_profile(request):
    if request.user.profile.role != 'employer':
        messages.error(request, "You do not have access to this page.")
        return redirect('home')
    return render(request, 'profile/employer.html', {'profile': request.user.profile})


@login_required
def edit_employer_profile(request):
    profile = request.user.profile
    if profile.role != 'employer':
        messages.error(request, "You do not have access to this page.")
        return redirect('home')
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('employer_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile/edit_employer.html', {'form': form})


# Job CRUD
@login_required
def job_create(request):
    if request.user.profile.role != 'employer':
        return redirect('home')
    
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job posting created successfully.')
            return redirect('job_list')
    else:
        form = JobPostingForm()
    return render(request, 'jobs/job_form.html', {'form': form})


@login_required
def job_edit(request, id):

    if request.user.profile.role != 'employer':
        return redirect('job_seeker')

    job = get_object_or_404(JobPosting, id=id)
    if request.method == 'POST':
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job posting updated successfully.')
            return redirect('job_list')
    else:
        form = JobPostingForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form, 'job': job})


@login_required
def job_delete(request, id):

    if request.user.profile.role != 'employer':
        return redirect('job_seeker')

    job = get_object_or_404(JobPosting, id=id)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job posting deleted')
        return redirect('job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})


# Applications
@login_required
def apply_for_job(request, id):
    job = get_object_or_404(JobPosting, id=id)

    if request.user.profile.role != 'job_seeker':
        messages.error(request, "Only job seekers can apply for jobs.")
        return redirect('job_list')
    if request.user.profile.role != 'job_seeker':
        return redirect('employer')
    
    job = get_object_or_404(JobPosting, id= id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.job_posting = job
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('job_list')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})


@login_required
def job_applications(request, id):
    job = get_object_or_404(JobPosting, id=id)
    if job.posted_by != request.user:
        messages.error(request, "You do not have access to view applications for this job.")
        return redirect('job_list')
    applications = Application.objects.filter(job_posting=job)
    return render(request, 'jobs/job_applications.html', {'job': job, 'applications': applications})


@login_required
def application_detail(request, id):
    application = get_object_or_404(Application, id=id)
    if application.applicant != request.user and application.job_posting.posted_by != request.user:
        messages.error(request, "You do not have access to this application.")
        return redirect('job_list')
    return render(request, 'jobs/application_detail.html', {'application': application})

@login_required
def all_job_applications(request):
    if request.user.profile.role != 'employer':
        messages.error(request, "Only employers can access this page.")
        return redirect('job_list')

    # Get all jobs posted by the employer
    jobs_posted = JobPosting.objects.filter(posted_by=request.user)

    # Get all applications for those jobs
    applications = Application.objects.filter(job_posting__in=jobs_posted)

    return render(request, 'jobs/all_job_applications.html', {'applications': applications})

@login_required
def user_applications(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'profile/user_applications.html', {'applications': applications})


# Job Search
def job_search(request):
    query = request.GET.get('q', '').strip()  # Get the search query 
    if not query:  # Adding If the query is blank, redirect to /jobs
        return redirect('job_list')
    results = JobPosting.objects.filter(title__icontains=query)  # Filter job postings by title
    return render(request, 'jobs/job_search.html', {'results': results, 'query': query})


#Job-page by id

def job_detail(request, id):
    job = get_object_or_404(JobPosting, id=id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def job_create(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user # to address the lack of posted_by FK
            form.save()
            return redirect('job_list')
    else:
        form = JobPostingForm()
    
    return render(request, 'jobs/job_create.html', {'form': form})

class JobUpdate(UpdateView):
    model = JobPosting
    fields = [
        'title',
        'description',
        'company_name',
        'company_description',
        'location',
        'salary'
        ]
    success_url = reverse_lazy('job_list')

class JobDelete(DeleteView):
    model = JobPosting
    success_url = '/jobs/'