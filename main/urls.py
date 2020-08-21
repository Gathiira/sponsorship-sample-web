from django.urls import path

from .views import home_page,applicant_home,staff_home,sponsor_home,success,approve_applicant,sponsor_applicant
urlpatterns = [
	path('', home_page, name='home_page'),
	path('applicant_index/',applicant_home, name='applicant_home'),
	path('staff_index/',staff_home, name='staff_home'),
	path('sponsor_index/',sponsor_home, name='sponsor_home'),
	path('success/',success, name='success'),

	path('staff_index/<int:pk>/',approve_applicant, name='approve_applicant'),
	path('sponsor_index/<int:pk>/',sponsor_applicant, name='sponsor_applicant'),
]