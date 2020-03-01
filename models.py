from django.db import models
from django.utils import timezone

# Create your models here.
class ContactForm(models.Model):
    full_name = models.CharField(max_length=300,blank=True)
    #This field store Email ID
    email_id = models.CharField(max_length=300,blank=True)
    #This field store Contact Number 
    contact_number = models.CharField(max_length=300,blank=True)
    #This field store Message 
    message = models.TextField(max_length=3000,blank=True)
    #This field store Date & Time at which form is submitted
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk) #Return Primary Key

    class Meta:
        verbose_name_plural = "Contact Form Data"
        verbose_name = "Contact Form"
