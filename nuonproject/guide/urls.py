# 小山 11/28-------------------------------------------
from django.urls import path
from . import views
from django.urls import path
from .views import AuthorizeCaseView, QRCodeView,CaseListView

app_name = 'guide'

# -----------------------------------------------------/
# 1/8小山-----------------------------------------------
urlpatterns = [
    path('caselist/', views.CaseListView.as_view(), name='caselist'),
    path('caselist/<int:case_id>/', CaseListView.comment_view, name='comment_view'),
    path('delete/', views.DeleteCaseView.as_view(), name='delete'),
    path('caseregistration/', views.CaseRegistrationView.as_view(), name='caseregistration'),
    # path('selectpref/', views.SelectPrefView.as_view(), name='selectpref'),
    path('guidancepindelete/', views.GuidancePinDeleteView.as_view(), name='guidancepindelete'),
    path('guidetop/', views.GuideTopView.as_view(), name='guidetop'),
    # koyama --------------------
    path('guidemap/', views.GuideMapView.as_view(), name='guidemap'),
    path('guidemap/<str:tour_number>/', views.GuideMapView.as_view(), name='guidemap'),
    
    # ---------------------------
    path('toursearch/', views.TourSearchView.as_view(), name='toursearch'),
    path('tour/<str:tour_number>/edit/', views.TourChangeView.as_view(), name='tourchange'),

    path("Informationpinchange/",views.InformationPinChangeView.as_view(),name="informationpinchange"),
    path("Informationpinregistration/",views.InformationPinRegistrationView.as_view(),name="informationpinregistration"),
    path("tourregistration/",views.TourRegistrationView.as_view(),name="tourregistration"),
    path("passwordchange/",views.PasswordChangeView.as_view(),name="passwordchange"),
    # path("caseregistconfirmation/",views.CaseRegistConfirmationView.as_view(),name="caseregistconfirmation"),
    # 根岸
    path('authorize_case/', AuthorizeCaseView.as_view(), name='authorize_case'),
    path('tour/<str:tour_number>/qr/', QRCodeView.as_view(), name='qr_code_view'),
    path('case/<str:case_number>/edit/', views.CaseUpdateView.as_view(), name='case_edit'),
    path('delete_comment/', views.DeleteCommentView.as_view(), name='delete_comment'),
    path('toursearch/namesearch/',views.TourNameListView.as_view(), name='toursearch/namesearch'),
    path('toursearch/numbersearch/',views.TourNumberListView.as_view(), name='toursearch/numbersearch'),
    path('caselist/titlesearch/',views.CaseTitleListView.as_view(), name='caselist/titlesearch'),
    path('caselist/sortesearch/',views.CaseSortListView.as_view(), name='caselist/sortsearch'),

]
# ---------------------------------------------------------
