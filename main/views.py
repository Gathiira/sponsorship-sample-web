from django.shortcuts import render,redirect
from .form import ApplicationForm
from django.contrib.auth.decorators import login_required
from accounts.models import User,Applicant,Staff,Sponsor
from django.contrib import messages
from .models import ApplicationModel
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def home_page(request):
    user = request.user
    if user.is_authenticated:
        if user.is_applicant:
            if user.applicant.has_applied:
                return redirect('/success')
            else:
                return redirect('/applicant_index')
        elif user.is_staff:
            return redirect('/staff_index')
        elif user.is_sponsor:
            return redirect('/sponsor_index')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def applicant_home(request):
    user = request.user
    applicant = Applicant.objects.get(user = user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            applicant.has_applied = True
            applicant.save(update_fields=['has_applied'])
            messages.success(request, 'Application submitted successfully!')
            return redirect('/success')
        else:
            messages.warning(request, 'OOPS!! Something went wrong ')
            return redirect('/success')
    else:
        form = ApplicationForm()
    return render(request, 'applicant_index.html',{'form': form,'applicant':applicant})


@login_required(login_url='/accounts/login/')
def success(request):
    return render(request, 'success.html')


@login_required(login_url='/accounts/login/')
def staff_home(request):
    if request.user.is_staff:
        applications = ApplicationModel.objects.all()
        return render(request, 'staff_index.html',{'applications': applications})
    else:
        return redirect('/')

@login_required(login_url='/accounts/login/')
def approve_applicant(request, pk):
    if request.user.is_staff:
        if request.method == 'POST':
            applicant = ApplicationModel.objects.get(pk=pk)
            applicant.is_approved = True
            applicant.save(update_fields=['is_approved'])
            subject = 'APPROVED APPLICATION'
            message = 'Your Application have been Approved sucessfully. GOOD luck attaining a sponsor'
            recepient = applicant.email
            send_mail(subject,message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
            return redirect('/staff_index')
        else:
            return redirect('/staff_index')
    else:
        return redirect('/')

@login_required(login_url='/accounts/login/')
def sponsor_home(request):
    if request.user.is_sponsor:
        applications = ApplicationModel.objects.all()
        return render(request, 'sponsor_index.html', {'applications':applications})
    else:
        return redirect('/')

@login_required(login_url='/accounts/login/')
def sponsor_applicant(request, pk):
    if request.user.is_sponsor:
        if request.method == 'POST':
            applicant = ApplicationModel.objects.get(pk=pk)
            applicant.is_sponsored = True
            applicant.save(update_fields=['is_sponsored'])
            subject = 'SPONSORED APPLICATION'
            message = 'Your Application have been sponsored by :' 
            message += '\nName \t:' + request.user.username
            message += '\nEmail \t:' + request.user.email
            message += '\nPhone Number \t:' + request.user.phone
            recepient = applicant.email
            send_mail(subject,message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
            return redirect('/sponsor_index')
        else:
            return redirect('/sponsor_index')
    else:
        return redirect('/')

