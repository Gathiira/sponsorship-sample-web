from django import forms
from .models import ApplicationModel

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = [
            'name','address','phone','email'
            ,'school_name','school_address','academic_level'
            ,'completion_year','reason','birth_certificate','national_id','recommendation_letter'
        ]