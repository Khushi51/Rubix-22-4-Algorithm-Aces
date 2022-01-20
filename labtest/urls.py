from django.urls import path

from . import views

urlpatterns = [
    path("tests_list", views.tests_list, name="tests-list"),
    path("<int:id>/confirm_test", views.confirm_test, name="confirm-test"),
    # path("savebill", views.labBill, name="savebill")
]