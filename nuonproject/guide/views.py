from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from .forms import CaseRegistrationForm, TourRegistrationForm,SearchForm,TourForm
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
from .models import Case, Tour, CustomUser,Category
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CommentForm

# 根岸
from django.http import HttpResponseForbidden, JsonResponse
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
        context['categories'] = Category.objects.all()  # カテゴリリストを追加
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

class DeleteCaseView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return JsonResponse({"status": "error", "message": "Permission denied"})

        try:
            data = json.loads(request.body)
            case_id = data.get("case_id")

            if not case_id:
                return JsonResponse({"status": "error", "message": "Case ID is missing"})

            case = Case.objects.get(case_number=case_id)
            case.delete()
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

class DeleteCommentView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return JsonResponse({"status": "error", "message": "Permission denied"})

        try:
            data = json.loads(request.body)
            comment_id = data.get("id")
            print(comment_id)

            if not comment_id:
                return JsonResponse({"status": "error", "message": "Case ID is missing"})

            comment = Comment.objects.get(id=comment_id)
            print(comment)
            comment.delete()
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

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

        import random

        # ランダムな8桁の数字を生成
        case_number = ''.join(random.choices('0123456789', k=8))  # 数字だけを8桁生成
        kwargs['initial'] = {'case_number': case_number}  # 初期値としてランダム事例番号を設定


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
    success_url = reverse_lazy('guide:toursearch')

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

        print(f"登録されたツアー番号: {tour.tour_number}")

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
            case.authorization = not case.authorization
            case.save()

            return JsonResponse({
                "status": "success",
                "authorization_status": case.authorization
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
class TourNameListView(ListView):
     model = Tour  # 表示対象のモデル
     template_name = 'TourSearch.html'  # 使用するテンプレート
     context_object_name = 'tourlist'  # テンプレート内で使う変数名

     def get_queryset(self):
         """
         検索キーワードに基づいて商品をフィルタリング
         """
         query = self.request.GET.get('q', '')  # クエリパラメータを取得
         if query:
             return Tour.objects.filter(tour_name__icontains=query)  # 部分一致検索
         return Tour.objects.all()  # 全件表示
     
class TourNumberListView(ListView):
     model = Tour  # 表示対象のモデル
     template_name = 'TourSearch.html'  # 使用するテンプレート
     context_object_name = 'tourlist'  # テンプレート内で使う変数名

     def get_queryset(self):
         """
         検索キーワードに基づいて商品をフィルタリング
         """
         query = self.request.GET.get('a', '')  # クエリパラメータを取得
         if query:
             return Tour.objects.filter(tour_number__icontains=query)  # 部分一致検索
         return Tour.objects.all()  # 全件表示
     
class CaseTitleListView(ListView):
     model = Case  # 表示対象のモデル
     template_name = 'CaseList.html'  # 使用するテンプレート
     context_object_name = 'caselist'  # テンプレート内で使う変数名

     def get_queryset(self):
         """
         検索キーワードに基づいて商品をフィルタリング
         """
         query = self.request.GET.get('b', '')  # クエリパラメータを取得
         if query:
             return Case.objects.filter(title__icontains=query)  # 部分一致検索
         return Case.objects.all()  # 全件表示
    
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
# GOOGLE_MAPS_API_KEY = 'AIzaSyBZEV4yAriodr076SoPrK5LAoVkuOhRX78'
# GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# 小山
class GuideMapView(View):
    # template_name = "GuideMap.html"

    def get(self, request, **kwargs):

        # HTMLに表示したいデータベースからの情報を取得
        sort = Sort.objects.all()
        tours = Tour.objects.all()
        guide_pins = GuidePin.objects.all()
        # info_pins = Information_pin.objects.all()

        # 前のページからツアー番号をgetで取得
        tour_number = request.GET.get('tour_number', None)
        
        api_key = 'AIzaSyBZEV4yAriodr076SoPrK5LAoVkuOhRX78'
        geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'

        print(f"取得した tour_number: {tour_number}")  # デバッグ用ログ
        if not tour_number:
            return JsonResponse({'error': 'tour_number is required'}, status=400)

        # 指定ツアーの案内ピン取得
        info_pins = Information_pin.objects.filter(tour_number=tour_number)
        data = []

        for pin in info_pins:
            geocode_params = {'address': pin.address, 'key': api_key}
            geocode_response = requests.get(geocode_url, params=geocode_params)
            geocode_result = geocode_response.json()

            if geocode_result['status'] == 'OK' and 'geometry' in geocode_result['results'][0]:
                location = geocode_result['results'][0]['geometry']['location']
                latitude = location['lat']
                longitude = location['lng']
            else:
                latitude = None
                longitude = None

            pin_data = {
                'id': pin.id,
                'place': pin.place,
                'explanation': pin.explanation,
                'address': pin.address,
                'latitude': latitude,
                'longitude': longitude,
                'image_url': pin.image.url if pin.image else '/media/images/no_image.png'
            }
            print(pin_data)
            data.append(pin_data)

        # HTMLに情報を送る
        return render(request, "GuideMap.html", {'sort_name': sort, 
                                                 'tours': tours,
                                                 'guide_pins': guide_pins,
                                                 'tour_number':tour_number,
                                                 'info_pins': json.dumps(data, ensure_ascii=False),
                                                 'select_tour_number':tour_number })
    
    def post(self, request, **kwargs):
        print("postで呼ばれました")

        pin_select = request.POST.get("pin_select")
        print(pin_select)
        print("-----------------------------")
        # tour_number = kwargs.get('tour_number')

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

            tour_number = Tour.objects.get(tour_number=request.POST.get("tour_number"))
            explanation = request.POST.get("explanation")
            address = request.POST.get("address")
            place = request.POST.get("place")
            image = request.FILES.get("image")

            print(explanation)
            print(address)
            print(place)
            print(image)

            Information_pin.objects.create(
                tour_number = tour_number,
                explanation = explanation,
                address = address,
                place = place,
                image = image
        )
            
        tour_number = self.request.POST.get("tour_number")
        redirect_url = reverse("guide:guidemap")
        redirect_url_tour_number = f"{redirect_url}?tour_number={tour_number}"
        return redirect(redirect_url_tour_number)
    

class CaseChangeView(UpdateView):
    model = Case
    form_class = CaseForm
    template_name = 'CaseChange.html'

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
    success_url = reverse_lazy('guide:toursearch')

    def get_object(self, queryset=None):
        tour_number = self.kwargs.get('tour_number')
        return get_object_or_404(Tour, tour_number=tour_number)
    def form_valid(self, form):
        # 投稿日は変更した日付に更新1
        tour = form.save(commit=False)
        tour.save()
        return redirect('/guide/toursearch/')
    
class CaseSortListView(ListView):
     model = Case  # 表示対象のモデル
     template_name = 'CaseList.html'  # 使用するテンプレート
     context_object_name = 'caselist'  # テンプレート内で使う変数名

     def get_queryset(self):
         """
         検索キーワードに基づいて商品をフィルタリング
         """
         category_id = self.request.GET.get('category', '')  # 選択したカテゴリID
         if category_id:
                return Case.objects.filter(category_id=category_id)
         return Case.objects.all()  # 全件表示
     
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # カテゴリリストを追加
        return context
     
    
class DeletePinView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return JsonResponse({"status": "error", "message": "Permission denied"})

        try:
            data = json.loads(request.body)
            pin_id = data.get("id")

            if not pin_id:
                return JsonResponse({"status": "error", "message": "Case ID is missing"})

            pin = Information_pin.objects.get(id=pin_id)
            pin.delete()
            return JsonResponse({'message': 'ピンが削除されました'}, status=200)

        except GuidePin.DoesNotExist:
            return JsonResponse({'error': '指定されたピンが存在しません'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'リクエストのパースに失敗しました'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'予期しないエラー: {str(e)}'}, status=500)
        

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from .models import Tour

class TourDeleteView(View):
    def post(self, request, tour_number):
        # ツアーを取得（存在しない場合は404エラー）
        tour = get_object_or_404(Tour, tour_number=tour_number)

        # ツアーの社員番号とログインユーザーの社員番号を比較
        if tour.number != request.user.number:
            messages.error(request, "このツアーを削除する権限がありません。")
            return redirect('guide:toursearch')  # 権限がない場合、ツアー検索ページへリダイレクト

        # ツアーを削除
        tour.delete()
        messages.success(request, 'ツアーが削除されました。')
        return redirect('guide:toursearch')  # 削除後、ツアー検索ページへリダイレクト
