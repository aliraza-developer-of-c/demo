
from django.contrib import admin
from .models import Contact, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'job_title', 'hire_date', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'department', 'job_title')
    list_filter = ('department', 'hire_date')

admin.site.register(Contact)
admin.site.register(Employee, EmployeeAdmin)



# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'department', 'job_title', 'hire_date', 'created_at', 'resume_link', 'contract_link')

#     def resume_link(self, obj):
#         if obj.resume:
#             return f'<a href="{obj.resume.url}">Download</a>'
#         return "No Resume"
    
#     def contract_link(self, obj):
#         if obj.contract:
#             return f'<a href="{obj.contract.url}">Download</a>'
#         return "No Contract"
    
#     resume_link.allow_tags = True
#     contract_link.allow_tags = True
