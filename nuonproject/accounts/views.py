from django.shortcuts import render

# 小山 1/7--------------------------------
from django.views.generic.base import TemplateView

from django.contrib.auth.views import LoginView
from django.urls import path
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages



# class SinInView(LoginView):
    # forms.py で定義したフォームスクラス
    # form_class = LogInForm
    # レンダリングするテンプレート
    # template_name = "Sinin.html"
    # def get_success_url(self):
    #     return reverse_lazy('main:index')

class PasswordDoneView(TemplateView):
    # ねぎしマサキンTV
    template_name = "PasswordDone.html"

class PasswordEmailView(TemplateView):
    # ねぎしマサキンTV
    template_name = "PasswordEmail.html"


class SinInView(LoginView):
    template_name = "Sinin.html"
    def form_valid(self, form):
        # ログイン後のリダイレクト先を管理者か一般ユーザーかで変更
        if self.request.user.is_superuser == True:
            print(self.request.user.is_superuser)
            return redirect('accounts:admin_dashboard')  # 管理者用のダッシュボードにリダイレクト
        else:
            print(self.request.user.is_superuser)
            return redirect('accounts:home')  
# ------------------------------------------/

# def admin_dashboard(request):
#     return render(request, 'manager/AdminTop.html')

# def home(request):
#     return render(request, 'guide/GuideTop.html')


