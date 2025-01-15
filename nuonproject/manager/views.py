from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from guide.models import CustomUser
from .forms import AccountCreationForm

# 清原 1/8--------------------------------
from django.views.generic.base import TemplateView

class AdminTopView(TemplateView):

    template_name = 'AdminTop.html'

class AdminViewView(TemplateView):
    # さくちゃんTV
    template_name = "AdminViewAccount.html"

# 1/15 あづまーと-------------------
class AdminCreateView(CreateView):
    model = CustomUser
    form_class = AccountCreationForm
    template_name = "AdminCreateAccount.html"  # 使用するテンプレート名
    success_url = reverse_lazy('manager:AdminTop')  # アカウント作成後にリダイレクトするURL
    
    # フォームが保存された後、パスワードをハッシュ化して保存する
    def form_valid(self, form):
        # 通常の保存処理を行う前にパスワードをハッシュ化
        password = form.cleaned_data.get('password')
        account = form.save(commit=False)  # 保存しない状態でインスタンスを取得
        account.set_password(password)  # パスワードをハッシュ化
        account.save()  # 保存
        return super().form_valid(form)
# --------------------------------

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
