from django.shortcuts import render
from django.urls import reverse
from .forms import CaseRegistrationForm
from django.views.generic.edit import FormView
from .models import Case

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

    # フォームが正常に送信された場合の処理
    def form_valid(self, form):
        # フォームのデータを処理（例：データベースへの保存など）
        title = form.cleaned_data['title']
        category = form.cleaned_data['category']
        content = form.cleaned_data['content']
        
        # ここでデータを保存することができます（例：モデルを使ってDB保存）
        return render(self.request, 'CaseRegistConfirmation.html', {
            'title': title,
            'category': category,
            'content': content
        })



    # フォーム送信後のリダイレクト先URLを指定
    def get_success_url(self):
        return reverse('guide:CaseRegistConfirmation')  # 登録成功後のページにリダイレクト


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

class CaseRegistConfirmationView(TemplateView):
    template_name = "CaseRegistConfirmation.html"

class homeView(TemplateView):
    template_name = 'GuideTop.html'