from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from .forms import CaseRegistrationForm, TourRegistrationForm,SearchForm,CommentForm
from django.views.generic.edit import FormView, CreateView
from .models import Case, Tour, CustomUser,Comment
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages

# 根岸
from django.http import JsonResponse
from django.views import View
import json

from django.http import JsonResponse
from guide.models import Information_pin  # guideアプリからインポート
import html

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
def get_pins(request):
    print('api実行')
    api_key = 'AIzaSyBZEV4yAriodr076SoPrK5LAoVkuOhRX78'
    geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    translate_url = 'https://translation.googleapis.com/language/translate/v2'
    pins = Information_pin.objects.all()
    data = []

    for pin in pins:
        print('========================================================================-')
        print('pin:', pin)

        # ジオコーディング
        geocode_params = {
            'address': pin.address,
            'key': api_key
        }
        geocode_response = requests.get(geocode_url, params=geocode_params)
        geocode_result = geocode_response.json()

        # レスポンスをログに記録
        print('Geocode API Response:', geocode_result)

        # ジオコーディング結果がOKか確認
        if geocode_result['status'] == 'OK' and 'geometry' in geocode_result['results'][0]:
            location = geocode_result['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
        else:
            # ジオコーディングに失敗した場合、nullのままとする
            latitude = None
            longitude = None


# さくちゃん 1/20
        # 翻訳処理
        translations = {}
        translations_explanation = {}
        for target_lang in ['en', 'zh', 'zh-TW', 'ko']:
            translate_params = {
                'q': html.escape(pin.place),
                'source': 'ja',
                'target': target_lang,
                'key': api_key
            }
            translate_response = requests.get(translate_url, params=translate_params)
            translate_result = translate_response.json()
            print(f'Translation API Response for {target_lang}:', translate_result)  # 追加
            if 'data' in translate_result and 'translations' in translate_result['data']:
                translations[target_lang] = html.unescape(translate_result['data']['translations'][0].get('translatedText', ''))
            else:
                print(f'Translation failed for {target_lang}: {translate_result}')
                translations[target_lang] = ''


            translate_params = {
                'q': html.escape(pin.explanation),
                'source': 'ja',
                'target': target_lang,
                'key': api_key
            }
            translate_response = requests.get(translate_url, params=translate_params)
            translate_result = translate_response.json()
            print(f'Translation API Response for {target_lang}:', translate_result)  # 追加
            if 'data' in translate_result and 'translations' in translate_result['data']:
                translations_explanation[target_lang] = html.unescape(translate_result['data']['translations'][0].get('translatedText', ''))
            else:
                print(f'Translation failed for {target_lang}: {translate_result}')
                translations_explanation[target_lang] = ''

        pin_data = {
            'place_ja': pin.place,
            'place_en': translations['en'],
            'place_zh': translations['zh'],
            'place_zh-TW': translations['zh-TW'],
            'place_ko': translations['ko'],
            'explanation_ja': pin.explanation,
            'explanation_en': translations_explanation['en'],
            'explanation_zh': translations_explanation['zh'],
            'explanation_zh-TW': translations_explanation['zh-TW'],
            'explanation_ko': translations_explanation['ko'],
            'address_ja': pin.address,
            'latitude': latitude,
            'longitude': longitude,
        }

        print(pin_data)  # デバッグ用：APIレスポンスを確認
        data.append(pin_data)

    return JsonResponse(data, safe=False)

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
    
    def form_valid(self, form):
        messages.success(self.request, '事例が登録されました')
        comment = form.save(commit=False)
        comment.number = self.request.user  # ユーザーを関連付け
        comment.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """ フォームが無効な場合の処理 """
        messages.error(self.request, "フォームにエラーがあります")
        print(form.errors)  # エラー内容を表示
        return super().form_invalid(form)