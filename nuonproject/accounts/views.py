from django.shortcuts import render

# 小山 1/7--------------------------------
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

class LoginView(TemplateView):

    template_name = 'index.html'

# ------------------------------------------/
