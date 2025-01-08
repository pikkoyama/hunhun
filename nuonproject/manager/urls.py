# 清原 1/8-------------------------------------------
from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [

    path(
        "admin/",
        views.AdminTopView.as_view(),
        name="admintop"
    ),
]
# -----------------------------------------------------/