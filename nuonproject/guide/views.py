from django.shortcuts import render
from django.urls import reverse
from .forms import CaseRegistrationForm
from django.views.generic.edit import FormView, CreateView
from .models import Case, Tour
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

# 根岸
from django.http import JsonResponse
from django.views import View
import json

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

# # フォームをビュー内で直接定義
# class CaseForm(forms.Form):
#     title = forms.CharField(max_length=100, label='タイトル')
#     category = forms.ChoiceField(
#         choices=[('category1', 'カテゴリ1'), ('category2', 'カテゴリ2'), ('category3', 'カテゴリ3')],
#         label='カテゴリ'
#     )
#     content = forms.CharField(widget=forms.Textarea, label='本文')

# フォーム送信後の処理とリダイレクトを行うクラスベースビュー
class CaseRegistrationView(FormView):
    template_name = 'CaseRegistration.html'
    form_class = CaseRegistrationForm  # 直接定義したフォームクラスを使用
    success_url = reverse_lazy('guide:caseregistconfirmation')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # 現在のログインユーザーをフォームに渡す
        return kwargs

    def form_valid(self, form):
        # フォームが有効な場合の処理
        case = form.save(commit=False)
        case.user = self.request.user  # ユーザーを関連付け
        case.save()
        return super().form_valid(form)
        
        # ここでデータを保存することができます（例：モデルを使ってDB保存）
        # return render(self.request, 'CaseRegistConfirmation.html', {
        #     'number': number,
        #     'title': title,
        #     'category': category,
        #     'post_date': post_date
    # })

    # # フォーム送信後のリダイレクト先URLを指定
    # def get_success_url(self):
    #     return reverse('guide:CaseRegistConfirmation')  # 登録成功後のページにリダイレクト

class CaseRegistConfirmationView(TemplateView):
    template_name = "CaseRegistConfirmation.html"

# class SelectPrefView(TemplateView):

#     template_name = 'SelectPref.html'

class GuidancePinDeleteView(TemplateView):

    template_name = 'GuidancePinDelete.html'

class GuideTopView(TemplateView):

    template_name = 'GuideTop.html'
# 個やア　1/20
class TourSearchView(TemplateView):

     def tourlist(request):
        # Caseテーブルのすべてのレコードを取得
        tourlist = Tour.objects.all() 
        # requestでcaselistをCaseList.htmlに渡す
        return render(request, 'TourSearch.html', {'tourlist': tourlist})

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

# 根岸 1/20
class AuthorizeCaseView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return JsonResponse({"status": "error", "message": "Permission denied"})

        try:
            data = json.loads(request.body)  # JSONを解析
            case_id = data.get("case_id")
            print("受け取ったcase_id:", case_id)

            if not case_id:
                return JsonResponse({"status": "error", "message": "Case ID is missing"})

            case = Case.objects.get(case_number=case_id)
            case.authonrization = not case.authonrization
            case.save()

            return JsonResponse({
                "status": "success",
                "authorization_status": case.authonrization
            })

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"})
        except Case.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Case not found"})