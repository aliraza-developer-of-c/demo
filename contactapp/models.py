from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField()
    department = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')  # Ensures the file is uploaded to the 'resumes' folder
    contract = models.FileField(upload_to='contracts/')  # For storing contract
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
