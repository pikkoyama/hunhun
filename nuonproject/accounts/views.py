from django.shortcuts import render

# 小山 1/7--------------------------------
from django.views.generic.base import TemplateView

from django.contrib.auth.views import LoginView
from django.urls import path

class SinInView(LoginView):
    # forms.py で定義したフォームスクラス
    # form_class = LogInForm
    # レンダリングするテンプレート
    template_name = "Sinin.html"
    # def get_success_url(self):
    #     return reverse_lazy('main:index')

class PasswordDoneView(TemplateView):
    # ねぎしマサキンTV
    template_name = "PasswordDone.html"

class PasswordEmailView(TemplateView):
    # ねぎしマサキンTV
    template_name = "PasswordEmail.html"
# ------------------------------------------/
