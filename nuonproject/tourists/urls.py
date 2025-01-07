# あづーま
from django.urls import path, include
from . import views

app_name = 'tourists'

urlpatterns = [
    path(
        "InformationPinChange/",
        views.InformationPinChangeView.as_view(),
        name="InformationPinChange"
    ),
    path(
        "InformationPinRegistration/",
        views.InformationPinRegistrationView.as_view(),
        name="InformationPinRegistration"
    ),
    path(
        "PasswordChange/",
        views.PasswordChangeView.as_view(),
        name="PasswordChange"
    ),
    path(
        "TourRegistration/",
        views.TourRegistrationView.as_view(),
        name="TourRegistration"
    )
]
# -----------------------------------------------------/