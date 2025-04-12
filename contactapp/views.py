from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Employee
from .forms import EmployeeForm

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, 'Your message has been sent!')
        return redirect('contact')

    return render(request, 'contact.html')
# employee_create

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)  # Include files (resume, contract)
        if form.is_valid():
            form.save()  # Save the employee data to the database
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')  # Redirect to the employee list page
    else:
        form = EmployeeForm()

    return render(request, 'employee_create.html', {'form': form})
# employee_list
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# home page
def home(request):
    return render(request, 'home.html')