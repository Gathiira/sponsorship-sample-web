from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Applicant,Staff,Sponsor

class ApplicantSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'phone', 'email']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_applicant = True
        user.save()
        applicant = Applicant.objects.create(user=user)
        applicant.has_applied = False
        applicant.save()
        return user

class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'phone', 'email']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        staff = Staff.objects.create(user=user)
        staff.save()
        return user

class SponsorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'phone', 'email']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_sponsor = True
        user.save()
        sponsor = Sponsor.objects.create(user=user)
        sponsor.save()
        return user