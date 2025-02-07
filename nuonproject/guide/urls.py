from django.urls import path
from . import views
from django.urls import path
from .views import AuthorizeCaseView, QRCodeView,CaseListView
from .views import DeletePinView

app_name = 'guide'

# 1/8小山-----------------------------------------------
# 2/7岩本-----------------------------------------------
urlpatterns = [
    # トップページ画面URL
    path('guidetop/',
         views.GuideTopView.as_view(),
         name='guidetop'),
    # パスワード変更URL
    path("passwordchange/",
         views.PasswordChangeView.as_view(),
         name="passwordchange"),

    # ---------事例関連URL-----------
    # 事例閲覧URL
    path('caselist/',
         views.CaseListView.as_view(),
         name='caselist'),
    # 事例コメントURL
    path('caselist/<int:case_id>/',
         CaseListView.comment_view,
         name='comment_view'),
    # 事例削除URL(管理者専用)
    path('delete/',
         views.DeleteCaseView.as_view(),
         name='delete'),
    # 事例登録URL
    path('caseregistration/',
         views.CaseRegistrationView.as_view(),
         name='caseregistration'),
    # 事例変更URL
    path('case/<str:case_number>/edit/',
         views.CaseChangeView.as_view(),
         name='case_edit'),
    # 事例タイトル検索URL
    path('caselist/titlesearch/',
         views.CaseTitleListView.as_view(),
         name='caselist/titlesearch'),
    # 事例ソート検索URL
    path('caselist/sortesearch/',
         views.CaseSortListView.as_view(),
         name='caselist/sortsearch'),
    # コメント削除URL(入力者専用)
    path('delete_comment/',
         views.DeleteCommentView.as_view(),
         name='delete_comment'),
    # 事例認可URL(管理者画面)
    path('authorize_case/',
         AuthorizeCaseView.as_view(),
         name='authorize_case'),

    # ---------ツアー関連URL-----------
    # ツアー閲覧URL
    path('toursearch/',
         views.TourSearchView.as_view(),
         name='toursearch'),
    # ツアー変更URL
    path('tour/<str:tour_number>/edit/',
         views.TourChangeView.as_view(),
         name='tourchange'),
    # ツアータイトル検索URL
    path('toursearch/namesearch/',
         views.TourNameListView.as_view(),
         name='toursearch/namesearch'),
    # ツアー番号検索URL
    path('toursearch/numbersearch/',
         views.TourNumberListView.as_view(),
         name='toursearch/numbersearch'),
    # ツアーQRコード表示URL
    path('tour/<str:tour_number>/qr/',
         QRCodeView.as_view(),
         name='qr_code_view'),
    # ツアー登録画面URL
    path("tourregistration/",
         views.TourRegistrationView.as_view(),
         name="tourregistration"),

    # ---------ガイドマップ関連URL-----------
    # ガイドマップURL
    path('guidemap/',
         views.GuideMapView.as_view(),
         name='guidemap'),
    # ガイドマップURL(ツアー別)
    path('guidemap/<str:tour_number>/',
         views.GuideMapView.as_view(),
         name='guidemap'),
    # ガイドピン登録URL
    path("Informationpinregistration/",
         views.InformationPinRegistrationView.as_view(),
         name="informationpinregistration"),
    # ガイドピン削除URL1
    path('delete_pin/',
         DeletePinView.as_view(),
         name='delete_pin'),

    path('tour/delete/<str:tour_number>/',
          views.TourDeleteView.as_view(), 
          name='delete_tour'),

]