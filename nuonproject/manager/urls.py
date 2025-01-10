# 清原 1/8-------------------------------------------
from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [

    path(
        "admintop/",
        views.AdminTopView.as_view(),
        name="AdminTop"
    ),

    path(
        "adminview/",
        views.AdminViewView.as_view(),
        name="AdminViewAccount"
    ),

    path(
        "admincreate/",
        views.AdminCreateView.as_view(),
        name="AdminCreateAccount"
    ),

    path(
        "adminsuccess/",
        views.AdminSuccessView.as_view(),
        name="AdminTransmissionComp"
    ),

    path(
        "casedelete/",
        views.CaseDeleteView.as_view(),
        name="CaseDelete"
    ),

    path(
        "accountdelete/",
        views.AccountDeleteView.as_view(),
        name="AccountDelete"
    ),


]
# -----------------------------------------------------/