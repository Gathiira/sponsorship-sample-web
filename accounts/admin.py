from django.contrib import admin
from .models import User, Applicant, Staff,Sponsor

admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(Staff)
admin.site.register(Sponsor)
