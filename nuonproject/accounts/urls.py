# 小山 1/7-------------------------------------------
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path(
        "sinin/",
        views.SinInView.as_view(),
        name="sinin"
    ),
]
# -----------------------------------------------------/