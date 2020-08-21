from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import ApplicantSignUpForm, StaffSignUpForm,SponsorSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class applicant_register(CreateView):
    model = User
    form_class = ApplicantSignUpForm
    template_name = 'applicant_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class sponsor_register(CreateView):
    model = User
    form_class = SponsorSignUpForm
    template_name = 'sponsor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                if user.is_applicant:
                    login(request,user)
                    return redirect('/applicant_index')
                elif user.is_staff:
                    login(request,user)
                    return redirect('/staff_index')
                elif user.is_sponsor:
                    login(request,user)
                    return redirect('/sponsor_index')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
