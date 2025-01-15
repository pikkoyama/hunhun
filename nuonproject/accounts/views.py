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

    def dispatch(self, request, *args, **kwargs):
        # すでにログイン済みの場合
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('accounts:admin_dashboard')  # 管理者用画面
            else:
                return redirect('accounts:home')  # 一般ユーザー画面
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        print("=================================================")
        print('is_superuser:',self.request.user.is_superuser)
        print('username:',self.request.user.username)       
        print("=================================================")
        # ログイン成功時のリダイレクト先を設定
        if self.request.user.is_superuser:
            return reverse_lazy('accounts:admin_dashboard')  # 管理者用ダッシュボード
        else:
            return reverse_lazy('accounts:home')  # 一般ユーザー画
# ------------------------------------------/
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    # ログアウト後のリダイレクト先を指定
    next_page = reverse_lazy('accounts:Sinin')  
# def admin_dashboard(request):
#     return render(request, 'manager/AdminTop.html')
# あーずま

# def home(request):
#     return render(request, 'guide/GuideTop.html')


