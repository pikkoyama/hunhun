from django.shortcuts import render

# 清原 1/8--------------------------------
from django.views.generic.base import TemplateView

class AdminTopView(TemplateView):

    template_name = 'AdminTop.html'

class AdminViewView(TemplateView):
    # さくちゃんTV
    template_name = "AdminViewAccount.html"

class AdminCreateView(TemplateView):
    # さくちゃんTV
    template_name = "AdminCreateAccount.html"

class AdminSuccessView(TemplateView):
    # さくちゃんTV
    template_name = "AdminTransmissionComp.html"

class CaseDeleteView(TemplateView):
    # さくちゃんTV
    template_name = "CaseDelete.html"

class AccountDeleteView(TemplateView):
    # さくちゃんTV
    template_name = "AccountDelete.html"

class admin_dashboardView(TemplateView):
    template_name = "AdminTop.html"



# ------------------------------------------/
