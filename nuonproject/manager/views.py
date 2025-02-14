from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from guide.models import CustomUser
from .forms import AccountCreationForm
from django.contrib import messages

#  1/8--------------------------------
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

class AdminTopView(TemplateView):

    template_name = 'AdminTop.html'

class AdminViewView(TemplateView):
    
    template_name = "AdminViewAccount.html"

# 1/15 -------------------
class AdminCreateView(CreateView):
    model = CustomUser
    form_class = AccountCreationForm
    template_name = "AdminCreateAccount.html"  # 使用するテンプレート名
    success_url = reverse_lazy('manager:AdminTop')  # アカウント作成後にリダイレクトするURL
    
    # フォームが保存された後、パスワードをハッシュ化して保存する
    def form_valid(self, form):
        # アカウント作成の後、フラッシュメッセージを設定
        messages.success(self.request, 'アカウントが作成されました。')
        # 通常の保存処理を行う前にパスワードをハッシュ化
        password = form.cleaned_data.get('password')
        account = form.save(commit=False)  # 保存しない状態でインスタンスを取得
        account.set_password(password)  # パスワードをハッシュ化
        account.save()  # 保存
        return super().form_valid(form)

# --------------------------------

class AdminSuccessView(TemplateView):
    
    template_name = "AdminTransmissionComp.html"

class CaseDeleteView(TemplateView):
    
    template_name = "CaseDelete.html"

class AccountDeleteView(TemplateView):
    
    template_name = "AccountDelete.html"

class admin_dashboardView(TemplateView):
    template_name = "AdminTop.html"


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from guide.models import CustomUser

@login_required
def guide_account_list(request):
    """ガイドアカウント一覧を表示するビュー"""
    guides = CustomUser.objects.filter(admin=False)  # 管理者ではないユーザーを表示
    return render(request, 'AdminViewAccount.html', {'guides': guides})

@login_required
def delete_guide_account(request, guide_id):
    """ガイドアカウントを削除するビュー"""
    messages.success(request, 'アカウントが削除されました。')
    guide = get_object_or_404(CustomUser, number=guide_id)
    guide.delete()
    return redirect('manager:guide_account_list')




# ------------------------------------------/
