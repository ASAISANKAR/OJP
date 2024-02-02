from django.db import models

# Create your models here.
class JobDetails(models.Model):
    work_title=models.CharField(max_length=255)
    salary_offered=models.CharField(max_length=255)
    JOB_TYPE =[
        ('fulltime','Full Time'),
        ('parttime','Part Time'),
        ('contract','Contract'),
    ]
    job_type=models.CharField(max_length=20,choices=JOB_TYPE)
    benefits=models.TextField()
    education=models.CharField(max_length=255)
    work_location=models.CharField(max_length=255)
    required_skills=models.TextField()

    def __str__(self):
        return self.work_title