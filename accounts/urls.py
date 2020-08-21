from django.urls import path
from . import views

urlpatterns=[
     path('applicant_register/',views.applicant_register.as_view(), name='applicant_register'),
     path('staff_register/',views.staff_register.as_view(), name='staff_register'),
     path('sponsor_register/',views.sponsor_register.as_view(), name='sponsor_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]