from django.shortcuts import render

# 我妻1/8--------------------------------
from django.views.generic.base import TemplateView

class InformationPinChangeView(TemplateView):
    # あづーま
    template_name = "InformationPinChange.html"

class InformationPinRegistrationView(TemplateView):
    # あづーま
    template_name = "InformationPinRegistration.html"

class PasswordChangeView(TemplateView):
    # あづーま
    template_name = "PasswordChange.html"

class TourRegistrationView(TemplateView):
    # あづーま
    template_name = "TourRegistration.html"
# ------------------------------------------/
