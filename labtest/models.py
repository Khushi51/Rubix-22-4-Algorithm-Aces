from re import T
from django.db import models
from appointment.models import Patient
# Create your models here.

class LabTests(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
   

    def __str__(self):
        return self.name

class LabBilling(models.Model):
    patientname = models.CharField(max_length=50,null=True)
    labtestname= models.CharField(max_length=50,null=True)
    bill = models.IntegerField(null=True)
    patient =models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    labTests =models.ForeignKey(
        LabTests, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.patient.name} {self.labTests.name}"

# Username (leave blank to use 'khushihotwani'): khushi
# Email address: 
# Password: saakhi
# Password (again): saakhi
# This password is too short. It must contain at least 8 characters.