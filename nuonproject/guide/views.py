from django.shortcuts import render
from django.urls import reverse
from .forms import CaseRegistrationForm
from django.views.generic.edit import FormView, CreateView
from django.views.generic import View
from .models import Case
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

# 小山 1/10--------------------------------
from django.views.generic.base import TemplateView
# 事例一覧を表示するビュー
class CaseListView(TemplateView):
    # 事例のデータをhtmlに渡す関数
    def caselist(request):
        # Caseテーブルのすべてのレコードを取得
        caselist = Case.objects.all() 
        # requestでcaselistをCaseList.htmlに渡す
        return render(request, 'CaseList.html', {'caselist': caselist})
    
    # template_name = "CaseList.html"

# ------------------------------------------/

# フォーム送信後の処理とリダイレクトを行うクラスベースビュー
class CaseRegistrationView(FormView):
    template_name = 'CaseRegistration.html'
    form_class = CaseRegistrationForm  # 直接定義したフォームクラスを使用
    success_url = reverse_lazy('guide:caseregistconfirmation')

    print("----------test1--------------------")

    def form_valid(self, form):
        print("----------test2--------------------")
        # ログイン中のユーザーのIDをセッションに保存
        user = self.request.user
        self.request.session['user_pk'] = user.pk  # ユーザーIDを保存

        # フォームデータをセッションに保存
        self.request.session['form_data'] = form.cleaned_data
        return redirect(self.success_url)

# 事例登録確認画面表示ビュー
class CaseRegistConfirmationView(View):
    def get(self, request, *args, **kwargs):
        # セッションからフォームデータとユーザーIDを取得
        form_data = request.session.get('form_data', None)
        user_pk = request.session.get('user_pk', None)
        
        if form_data and user_pk:
            # ユーザーIDを使ってユーザーオブジェクトを取得
            User = get_user_model()
            print(User)
            user = User.objects.get(id=user_pk)
            
            return render(request, 'GuideTop.html', {
                'form_data': form_data,
                'user': user  # ユーザー情報もテンプレートに渡す
            })
        
    def post(self, request, *args, **kwargs):
        form_data = request.session.get('form_data', None)
        user_pk = request.session.get('user_pk', None)

        if form_data and user_pk:
            # ユーザーpkを使ってユーザーオブジェクトを取得
            User = get_user_model()
            user = User.objects.get(pk=user_pk)

            # データベースに登録
            case = Case.objects.create(
                case_number=form_data['case_number'],
                number=form_data['number'],
                title=form_data['title'],
                category=form_data['category'],
                main=form_data['main'],
                post_date=form_data['post_date'],
                user=user  # ユーザーオブジェクトを関連付け
            )

            # セッションからデータを削除
            del request.session['form_data']
            del request.session['user_pk']

            return redirect('guidetop')  # 完了ページにリダイレクト
        return redirect('caseregistration')
    
class SelectPrefView(TemplateView):

    template_name = 'SelectPref.html'

class GuidancePinDeleteView(TemplateView):

    template_name = 'GuidancePinDelete.html'

# class GuideTopView(TemplateView):

    # template_name = 'GuideTop.html'

class TourSearchView(TemplateView):

    template_name = 'TourSearch.html'

class InformationPinChangeView(TemplateView):
    # あづーま
    template_name = "InformationPinChange.html"

class InformationPinRegistrationView(TemplateView):
    # あづーま
    template_name = "InformationPinRegistration.html"

class TourRegistrationView(TemplateView):
    # あづーま
    template_name = "TourRegistration.html"

class PasswordChangeView(TemplateView):
    # あづーま
    template_name = "PasswordChange.html"



class homeView(TemplateView):
    template_name = 'GuideTop.html'