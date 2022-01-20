import email
import imp
import re
from django.shortcuts import redirect, render
from .models import LabTests
from .models import LabBilling,Patient
# Create your views here.

def tests_list(request):
    lst = LabTests.objects.all()
    selected = False
    return render(request, "labtest/tests_list.html",{
        "tests_list": lst,
        "selected": selected
    })

def confirm_test(request, id):
    tests = LabTests.objects.all()[0]
    # patient_detail = tests.patient.all()
    test = LabTests.objects.get(id=id)

    current_user=request.user
    patient = Patient.objects.get(email=current_user.email)
    

    # lab=get it from labname

    print(patient)
    if request.method == 'POST':
        print('Post request done')
        # patientname= request.POST.get('test.patient.name')
        labtestname= request.POST.get('labtest')
        print(labtestname)
        labtest=LabTests.objects.get(name=labtestname)
        # bill= request.POST.get('test.price')
        en = LabBilling(patient=patient, labTests=labtest,)
        en.save()
        return redirect('/labtesttests_list')
    else:
        print('post is not seen')

    # return render(request, "labtest/confirm_test.html")

    return render(request, "labtest/confirm_test.html", {
        # "patient_details":patient_detail,
        "test":test
    })

# def labBill(request):
#     current_user=request.user
#     patient = Patient.objects.get(email=current_user.email)
    

#     # lab=get it from labname
#     if request.method=="POST":
#         patientname= request.POST.get('test.patient.name')
#         labtestname= request.POST.get('labtest')
#         print(labtestname)
#         labtest=LabTests.objects.get(name=labtestname)
#         bill= request.POST.get('test.price')
#         en = LabBilling(patient=patient, labTests=labtest, bill=bill)
#         en.save()

#     return render(request, "labtest/confirm_test.html")

