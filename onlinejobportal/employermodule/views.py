from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *



from jobseekermodule.models import JobApplication


# Create your views here.
@login_required(login_url='login1')
def projecthomepage(request):
    return render(request,'employerhomepage.html')
@login_required(login_url='login1')
def jobpost(request):
    return render(request,'jobpost.html')
@login_required(login_url='login1')
def add_job_details(request):
    if request.method=='POST':
        work_title=request.POST.get('workTitle')
        salary_offered=request.POST.get('salary_offered')
        job_type=request.POST.get('job_type')
        benefits=request.POST.get('benefits')
        education=request.POST.get('education')
        work_location=request.POST.get('work_location')
        required_skills=request.POST.get('required_skills')

        job_details=JobDetails(
            work_title=work_title,
            salary_offered=salary_offered,
            job_type=job_type,
            benefits=benefits,
            education=education,
            work_location=work_location,
            required_skills=required_skills,
        )
        job_details.save()
        return redirect('view_job_details')
    return render(request,'jobpost.html')
@login_required(login_url='login1')
def view_job_details(request):
    job_details_list=JobDetails.objects.all()
    return render(request,'view_job_details.html',{'job_details_list':job_details_list})

@login_required(login_url='login1')
def edit(request,pk):
    job_details = JobDetails.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            job_details.work_title = request.POST['workTitle']
            job_details.salary_offered = request.POST['salaryOffered']
            job_details.job_type = request.POST['jobType']
            job_details.benefits = request.POST['benefits']
            job_details.education = request.POST['education']
            job_details.work_location = request.POST['workLocation']
            job_details.required_skills = request.POST['requiredSkills']
            job_details.save()
            return redirect('view_job_details')


    return render(request,'edit_job_details.html',{'job_details':job_details})

@login_required(login_url='login1')
def remove(request, pk):
    try:
        employee = get_object_or_404(JobDetails, id=pk)
        employee.delete()
        return redirect('view_job_details')
    except JobDetails.DoesNotExist:
        return HttpResponse("Employee not found", status=404)

@login_required(login_url='login1')
def job_application_list(request):
    job_application=JobApplication.objects.all()
    return render(request,'job_application_list.html',{'job_application':job_application})






