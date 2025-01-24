from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

# 小山 1/7--------------------------------


class ChangePasswordView(TemplateView):
    def get(self, request):
        return render(request, 'change_password.html')

    def post(self, request):
        email = request.POST.get('email')

        # メールアドレスからユーザーを取得（カスタムユーザーを使用）
        User = get_user_model()  # ここでカスタムユーザーモデルを取得
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "そのメールアドレスのユーザーは存在しません。")
            return redirect('accounts:change_password')

        # トークンとUIDを生成してメール送信
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        reset_url = request.build_absolute_uri(reverse('accounts:password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))


        # メールの内容を作成
        subject = "パスワード変更のリクエスト"
        message = render_to_string('password_reset_email.html', {
            'user': user,
            'reset_url': reset_url,
        })

        # HTML形式のメールを送信
        send_mail(
            subject,
            message,
            'oom2325066@stu.o-hara.ac.jp',  # 送信者のメールアドレス
            [user.email],  # 受信者のメールアドレス
            html_message=message  # HTMLメールとして送信
        )

        return redirect('accounts:password_reset_done')

class PasswordResetConfirmView(TemplateView):
    def get(self, request, uidb64, token):
        try:
            # uidb64をデコードしてユーザーのIDを取得
            uid = urlsafe_base64_decode(uidb64).decode()  # バイトデータをデコード
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            # エラーが発生した場合は、無効なリンクメッセージを表示してリダイレクト
            messages.error(request, "無効なリンクです。")
            return redirect('accounts:change_password')

        if not default_token_generator.check_token(user, token):
            # トークンが無効な場合もエラーメッセージ
            messages.error(request, "無効なトークンです。")
            return redirect('accounts:change_password')

        # パスワードリセットフォームを表示
        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {
    'form': form,
    'uidb64': uidb64,
    'token': token,
})

    def post(self, request, uidb64, token):
        try:
            # uidb64をデコードしてユーザーのIDを取得
            uid = urlsafe_base64_decode(uidb64).decode()  # バイトデータをデコード
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            # エラーが発生した場合は、無効なリンクメッセージを表示してリダイレクト
            messages.error(request, "無効なリンクです。")
            return redirect('accounts:change_password')

        if not default_token_generator.check_token(user, token):
            # トークンが無効な場合もエラーメッセージ
            messages.error(request, "無効なトークンです。")
            return redirect('accounts:change_password')

        # 新しいパスワードを設定
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "パスワードが正常に変更されました。")
            return redirect('accounts:PasswordDone')
        else:
            return render(request, 'password_reset_confirm.html', {
    'form': form,
    'uidb64': uidb64,
    'token': token,
})

class PasswordDoneView(TemplateView):
    # ねぎしマサキンTV
    template_name = "PasswordDone.html"

class PasswordEmailView(TemplateView):
    # ねぎしマサキンTV
    template_name = "PasswordEmail.html"

class PasswordResetDoneView(TemplateView):
    # あづーま
    template_name = "password_reset_done.html"

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
            return reverse_lazy('accounts:home')  # 一般ユーザー画面

    # フォームが無効な場合の処理
    def form_invalid(self, form):
        # ログイン失敗時のエラーメッセージを表示
        messages.error(self.request, "社員番号またはパスワードが間違っています。")
        return super().form_invalid(form)
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


