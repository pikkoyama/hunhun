# 小山 11/28-------------------------------------------
from django.urls import path
from . import views
from django.urls import path
from .views import AuthorizeCaseView, QRCodeView

app_name = 'guide'

# -----------------------------------------------------/
# 1/8小山-----------------------------------------------
urlpatterns = [
    path('caselist/', views.CaseListView.caselist, name='caselist'),
    path('caseregistration/', views.CaseRegistrationView.as_view(), name='caseregistration'),
    # path('selectpref/', views.SelectPrefView.as_view(), name='selectpref'),
    path('guidancepindelete/', views.GuidancePinDeleteView.as_view(), name='guidancepindelete'),
    path('guidetop/', views.GuideTopView.as_view(), name='guidetop'),
    # koyama --------------------
    path('guidemap/', views.GuideMapView.as_view(), name='guidemap'),
    path('api/pins/', views.get_pins, name='get_pins'),
    # ---------------------------
    path('toursearch/', views.TourSearchView.as_view(), name='toursearch'),

    path("Informationpinchange/",views.InformationPinChangeView.as_view(),name="informationpinchange"),
    path("Informationpinregistration/",views.InformationPinRegistrationView.as_view(),name="informationpinregistration"),
    path("tourregistration/",views.TourRegistrationView.as_view(),name="tourregistration"),
    path("passwordchange/",views.PasswordChangeView.as_view(),name="passwordchange"),
    # path("caseregistconfirmation/",views.CaseRegistConfirmationView.as_view(),name="caseregistconfirmation"),
    # 根岸
    path('authorize_case/', AuthorizeCaseView.as_view(), name='authorize_case'),
    path('tour/<str:tour_number>/qr/', QRCodeView.as_view(), name='qr_code_view'),
]
# ---------------------------------------------------------
