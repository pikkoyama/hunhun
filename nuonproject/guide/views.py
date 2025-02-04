from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from .forms import CaseRegistrationForm, TourRegistrationForm,SearchForm,TourForm
from django.views.generic.edit import FormView, CreateView
from .models import Case, Tour, CustomUser
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CommentForm

# 根岸
from django.http import JsonResponse
from django.views import View
import json

from django.http import JsonResponse
from guide.models import Information_pin, GuidePin, Sort  # guideアプリからインポート
import html, requests

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.utils import timezone
from django.views.generic.edit import UpdateView
from .models import Case
from .forms import CaseForm


# 小山 1/10--------------------------------
from django.views.generic.base import TemplateView
# 事例一覧を表示するビュー
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Case, Comment
from .forms import CommentForm

class CaseListView(FormView):
    template_name = 'Caselist.html'
    form_class = CommentForm  # 直接定義したフォームクラスを使用
    success_url = reverse_lazy('guide:caselist')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caselist'] = Case.objects.all()  # 事例データを取得
        for case in context['caselist']:
            case.comments = Comment.objects.filter(case_number=case.case_number)
        context['comments'] = Comment.objects.all()  # コメントデータを取得
        return context
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # 現在のログインユーザーをフォームに渡す
        return kwargs
    def comment_view(request, case_id):
        case = get_object_or_404(Case, id=case_id)  # case_idを使ってCaseオブジェクトを取得
        if request.method == 'POST':
            form = CommentForm(request.POST, user=request.user)
            form.fields['case_number'].initial = case  # ここでcase_numberをフォームにセット
            if form.is_valid():
                # フォームが有効ならコメントを保存
                comment = form.save(commit=False)
                comment.number = request.user  # コメントを投稿したユーザーをセット
                comment.save()
                return redirect('guide:comment_view')  # 成功後、事例一覧にリダイレクト
        else:
            form = CommentForm(user=request.user)
            form.fields['case_number'].initial = case  # 初期値としてcase_numberをセット
        return render(request, 'comment_form.html', {'form': form, 'case': case})
    def form_valid(self, form):
        messages.success(self.request, '事例が登録されました')
        comment = form.save(commit=False)
        comment.number = self.request.user  # ユーザーを関連付け
        comment.save()
        return super().form_valid(form)
    # 削除処理
    def delete_case(self, request, case_id):
        # case_idを使って該当のCaseオブジェクトを取得
        case = get_object_or_404(Case, id=case_id)
        
        # Caseオブジェクトを削除
        case.delete()

        # 削除成功のレスポンスを返す
        return JsonResponse({"status": "success"})

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
    success_url = reverse_lazy('guide:guidetop')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # 現在のログインユーザーをフォームに渡す
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, '事例が登録されました')
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

# class CaseRegistConfirmationView(TemplateView):
#     template_name = 'CaseRegistration.html'
#     form_class = CaseRegistrationForm  # 直接定義したフォームクラスを使用
#     success_url = reverse_lazy('guide:caseregistration')

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user  # 現在のログインユーザーをフォームに渡す
#         return kwargs

#     def form_valid(self, form):
#         # フォームが有効な場合の処理
#         case = form.save(commit=False)
#         case.user = self.request.user  # ユーザーを関連付け
#         case.save()
#         return super().form_valid(form)

# class SelectPrefView(TemplateView):

#     template_name = 'SelectPref.html'

class GuidancePinDeleteView(TemplateView):

    template_name = 'GuidancePinDelete.html'

class GuideTopView(TemplateView):

    template_name = 'GuideTop.html'

class GuideMapView(TemplateView):
    template_name='GuideMap.html'

# koyama　1/20
class TourSearchView(TemplateView):
    #  とりあえずツアー一覧表示
     template_name = 'TourSearch.html'

     def get_context_data(self, **kwargs):
        # 親クラスのget_context_dataを呼び出す
        context = super().get_context_data(**kwargs)
        # Tourテーブルのすべてのレコードを取得してcontextに追加
        context['tourlist'] = Tour.objects.all()
        return context

    #  template_name = 'TourSearch.html'
     
class TourRegistrationView(FormView):
    # 小山
    template_name = "TourRegistration.html"
    
    form_class = TourRegistrationForm  # 直接定義したフォームクラスを使用
    success_url = reverse_lazy('guide:guidemap')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # 現在のログインユーザーをフォームに渡す
        return kwargs

    def form_valid(self, form):
      # フォームが有効な場合の処理
        tour = form.save(commit=False)
        
        # ユーザーを自動的に関連付け（社員番号は不要）
        tour.user = self.request.user  # ログインユーザーを関連付け
        tour.number = self.request.user  # `number` フィールドには現在のログインユーザーを設定

        # debug
        print(f"1{tour.user}---------------------------")
        print(f"2{tour.number}---------------------------")

        # 保存
        tour.save()

        messages.success(self.request, "登録が完了しました")
        return super().form_valid(form)
    # エラー探し用のコード
    def form_invalid(self, form):
        # フォームが無効な場合の処理
        #print("フォームのエラー: ", form.errors)  # エラー内容を出力
        return super().form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "ツアー番号が重複しています")
        return super().form_invalid(form)
    
    # def form_invalid(self, form):
    #     messages.error(self.request, "この日付では登録できません")
    #     return super().form_invalid(form)

class InformationPinChangeView(TemplateView):
    # あづーま
    template_name = "InformationPinChange.html"

class InformationPinRegistrationView(TemplateView):
    # あづーま
    template_name = "InformationPinRegistration.html"

class PasswordChangeView(TemplateView):
    # あづーま
    template_name = "PasswordChange.html"

class homeView(TemplateView):
    template_name = 'GuideTop.html'

# 我妻2/4
class AuthorizeCaseView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return JsonResponse({"status": "error", "message": "Permission denied"})

        try:
            data = json.loads(request.body)
            case_id = data.get("case_id")

            if not case_id:
                return JsonResponse({"status": "error", "message": "Case ID is missing"})

            case = Case.objects.get(case_number=case_id)
            case.authonrization = not case.authonrization
            case.save()

            return JsonResponse({
                "status": "success",
                "authorization_status": case.authonrization
            })

        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            return JsonResponse({"status": "error", "message": "Invalid JSON format"})
        except Case.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Case not found"})
        except Exception as e:
            print(f"Unexpected error: {e}")
            return JsonResponse({"status": "error", "message": "An unexpected error occurred"})
################################
class SearchView(View):
    def search_view(request):
        """
        同じ画面で検索フォームと結果を表示するビュー関数。
        """
        posts = None  # 検索結果を格納する変数
        
        # POSTリクエストの場合、検索処理を実行
        if request.method == 'POST':
            form = SearchForm(request.POST)  # POSTデータをフォームにバインド
            if form.is_valid():
                keyword = form.cleaned_data['keyword']  # キーワードを取得
                # 部分一致でデータをフィルタリング
                posts = Tour.objects.filter(content__icontains=keyword)
        else:
            form = SearchForm()  # 初回アクセス時は空のフォームを表示

        # 検索フォームと結果を同じテンプレートに渡してレンダリング
        return render(request, 'search.html', {'form': form, 'posts': posts})
    
# ねぎし
from django.http import HttpResponse

from io import BytesIO
from django.urls import reverse
# import qrcode
class QRCodeView(TemplateView):
    template_name = "qr_code_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour_number = kwargs.get('tour_number')  # URLからツアー番号を取得
        tour = get_object_or_404(Tour, tour_number=tour_number)
        context['tour_name'] = tour.tour_name
        context['tour_number'] = tour.tour_number
        
        # ドメイン名を含めてフルURLを生成
        url = settings.SITE_URL + reverse('tourists:LanguageSelect')+ f"?tour_number={tour_number}"
        
        # 生成されたフルURLをログに出力
        print(f"生成されたQRコード用URL: {url}")
        
        # QRコードに渡すURLを設定
        context['qr_url'] = url
        
        return context
    
from django.shortcuts import get_object_or_404

class QRCodePageView(TemplateView):
    template_name = "qr_code_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour_number = kwargs.get("tour_number")
        tour = get_object_or_404(Tour, tour_number=tour_number)

        # QRコード用のURLを渡す
        context["qr_url"] = f"https://example.com/tour/{tour_number}/details"
        context["tour_name"] = tour.tour_name
        return context

# --------koyama---------------------------------------------------------
# Google Maps API設定
GOOGLE_MAPS_API_KEY = 'AIzaSyBZEV4yAriodr076SoPrK5LAoVkuOhRX78'
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

class GuideMapView(View):
    # template_name = "GuideMap.html"

    def get(self, request):

        sort = Sort.objects.all()
        tour = Tour.objects.filter('tour_number')
        return render(request, "GuideMap.html", {'sort_name':sort},{'tour_number':tour})
    
    def post(self, request, **kwargs):
        print("postで呼ばれました")

        pin_select = request.POST.get("pin_select")
        tour_number = kwargs.get('tour_number')

        if pin_select == "guide":

            sort_name = Sort.objects.get(id=request.POST.get("sort_name"))
            longitude = request.POST.get("longitude")
            latitude = request.POST.get("latitude")

            print(longitude)
            print(latitude)
            print(sort_name)
            print(pin_select)
        
            GuidePin.objects.create(

            number = self.request.user,
            sort = sort_name,
            longitude = longitude,
            latitude = latitude

        )
        
        else:

            information_pin_id = request.POST.get("longitude")
            explanation = request.POST.get("explanation")
            address = request.POST.get("address")
            place = request.POST.get("place")
            image = request.POST.get("image")

            print(information_pin_id)
            print(explanation)
            print(address)
            print(place)
            print(image)

        
            Information_pin.objects.create(
                information_pin_id = information_pin_id,
                tour_number = tour_number,
                explanation = explanation,
                address = address,
                place = place,
                image = image
        )

        

        return redirect("guide:guidemap")
    

class CaseUpdateView(UpdateView):
    model = Case
    form_class = CaseForm
    template_name = 'CaseUpdate.html'

    def get_object(self, queryset=None):
        case_number = self.kwargs.get('case_number')
        return get_object_or_404(Case, case_number=case_number)

    def form_valid(self, form):
        # 投稿日は変更した日付に更新
        case = form.save(commit=False)
        case.post_date = timezone.now()
        case.save()
        return redirect('/guide/caselist/')

class TourChangeView(UpdateView):
    model = Tour
    form_class = TourForm
    template_name = 'TourChange.html'

    def get_object(self, queryset=None):
        tour_number = self.kwargs.get('tour_number')
        return get_object_or_404(Case, tour_number=tour_number)
    def form_valid(self, form):
        # 投稿日は変更した日付に更新
        tour = form.save(commit=False)
        tour.save()
        return redirect('/guide/tourseach/')