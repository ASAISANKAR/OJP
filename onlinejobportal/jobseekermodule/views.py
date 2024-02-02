from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from employermodule.models import JobDetails

from .models import *
from .forms import *


# Create your views here.

@login_required(login_url='login1')
def projecthomepage(request):
    return render(request,'jobseekerhomepage.html')
@login_required(login_url='login1')
def viewjobs(request):
    return render(request,'viewjobs.html')

@login_required(login_url='login1')
def job_details_list(request):
    job_details_list=JobDetails.objects.all()
    return render(request,'viewjobs.html',{'job_details_list':job_details_list})

@login_required(login_url='login1')
def addjobseekerprofile(request):
    return render(request,'jobseekerprofile.html')

@login_required(login_url='login1')
def submit_form(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone_number=request.POST['phone_number']
        address=request.POST['address']
        tenth_marks=request.POST['10thMarks']
        twelth_marks=request.POST['12thMarks']
        cgpa=request.POST['cgpa']
        expected_salary=request.POST['expectedSalary']
        position=request.POST['position']

        applicant=Applicant(first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,tenth_marks=tenth_marks,twelth_marks=twelth_marks,cgpa=cgpa, expected_salary=expected_salary,position=position)
        applicant.save()
        return render(request, 'jobseekerhomepage.html')
    return render(request, 'jobseekerprofile.html')


def apply_to_job(request,job_id):
    job_details=get_object_or_404(JobDetails,id=job_id)
    if request.method=='POST':
        form=JobApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            job_application=form.save(commit=False)
            job_application.job_details=job_details
            job_application.save()

            subject='Job Application Received'
            message=('Thank you for applying to the Job. Your Application is received and will be sent to the next Process.\n\n'
                     f'Your Details\n'
                     f'Name: {job_application.name}\n\n\n\n'
                     
                     'Copyright A Sai Sankar - KLU. All rights reserved')
            from_email='saisankar3193@gmail.com'
            recipient_list=[job_application.email]
            send_mail(subject,message,from_email,recipient_list)
        return redirect('job_details_list')
    else:
        form=JobApplicationForm()

    return render(request,'apply_to_job.html',{'job_details':job_details,'form':form})

