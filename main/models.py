from django.db import models
import datetime

# Create your models here.

class ApplicationModel(models.Model):
    PRIMARY = 'PRI'
    SECONDARY = 'SEC'
    GRADUATE = 'GRAD'
    ACADEMIC_LEVEL_CHOICES = [
        (PRIMARY, 'Primary'),
        (SECONDARY, 'Secondary'),
        (GRADUATE, 'Graduate'),
    ]

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    school_name = models.CharField(max_length=20)
    school_address = models.CharField(max_length=20)
    academic_level = models.CharField(max_length=4,choices=ACADEMIC_LEVEL_CHOICES,default=PRIMARY)
    completion_year = models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year)
    reason = models.TextField(help_text='Tell us why we should sponsor you')
    birth_certificate= models.FileField(upload_to='docs/')
    national_id= models.FileField(upload_to='docs/')
    recommendation_letter= models.FileField(upload_to='docs/')
    
    is_approved = models.BooleanField(default=False)
    is_sponsored = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def approve(self):
        self.is_approved = True

    def sponsor(self):
        self.is_sponsored = True
