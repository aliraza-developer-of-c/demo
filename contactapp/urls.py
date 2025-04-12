from django.urls import path
from .views import contact_view, employee_list, employee_create, home

urlpatterns = [
    path('contact_us', contact_view, name='contact'),
    path('add_employee/', employee_create, name='add_employee'),
    path('employee_list/', employee_list, name='employee_list'),
    path('home/', home, name='home'),
    



]
