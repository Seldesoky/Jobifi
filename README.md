# Jobifi
https://imgur.com/WeThKER.png 

Jobifi is a Django-based job portal designed to connect job seekers and employers in a seamless way. The platform allows users to register as either job seekers or employers, manage their profiles, and apply for or post jobs.

---

## Features

### General Features
- **User Authentication**: Registration, login, and logout functionalities with role-based access control (Job Seeker/Employer).
- **Responsive Design**: Optimized for both desktop and mobile viewing.

### For Employers
- **Profile Management**: Edit profile details including company bio and logo.
- **Job Postings**: Create, update, delete, and view job postings.
- **Applications**:
  - View all applications received for a job posting.
  - Access details of each application, including applicant information and resumes.

### For Job Seekers
- **Profile Management**: Edit personal profile details.
- **Job Search**: Search jobs by title.
- **Applications**:
  - Apply for available job postings.
  - View jobs they have applied for.

---

## Installation and Setup

### Prerequisites
1. Python 3.10+
2. PostgreSQL
3. Virtualenv (recommended for environment isolation)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Jobifi
   ```

2. Set up the virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` file with the following:
   ```env
   DEBUG=True
   SECRET_KEY=<your-secret-key>
   DATABASE_NAME=<your-db-name>
   DATABASE_USER=<your-db-user>
   DATABASE_PASSWORD=<your-db-password>
   DATABASE_HOST=127.0.0.1
   DATABASE_PORT=5432
   ```

5. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000/`.

---

## Deployment

//TBD//

## Version
V.01

---

## Core Functionalities

### User Registration and Authentication
- Users can register with a username, email, password, and role selection.
- Role-based views restrict access to specific functionalities (e.g., only job seekers can apply for jobs).

### Job Postings
- Employers can create job postings with details such as title, description, salary, location, and company information.
- Job seekers can browse or search for job postings.

### Applications
- Job seekers can apply for jobs with a cover letter and upload a resume.
- Employers can view all applications for jobs they have posted.

---

## Contributing
We welcome contributions! Please fork this repository, create a new branch, and submit a pull request.

