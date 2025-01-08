# 清原 1/8-------------------------------------------
from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [

    path(
        "admintop/",
        views.AdminTopView.as_view(),
        name="admintop"
    ),

    path(
        "adminview/",
        views.AdminViewView.as_view(),
        name="adminviewaccount"
    ),

    path(
        "admincreate/",
        views.AdminCreateView.as_view(),
        name="admincreateaccount"
    ),

    path(
        "adminsuccess/",
        views.AdminSuccessView.as_view(),
        name="admintransmissioncomp"
    ),

    path(
        "casedelete/",
        views.CaseDeleteView.as_view(),
        name="casedelete"
    ),

    path(
        "accountdelete/",
        views.AccountDeleteView.as_view(),
        name="accountdelete"
    ),


]
# -----------------------------------------------------/