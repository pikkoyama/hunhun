# 小山 11/28-------------------------------------------
from django.urls import path
from . import views

app_name = 'guide'

# -----------------------------------------------------/
# 1/8小山-----------------------------------------------
urlpatterns = [
    path('caselist/', views.CaseListView.as_view(), name='caselist'),
    path('caseRegistration/', views.CaseRegistrationView.as_view(), name='caseregistration'),
    path('ExampleView/', views.ExampleViewView.as_view(), name='exampleview'),
    path('GuidancePinDelete/', views.GuidancePinDeleteView.as_view(), name='guidancepindelete'),
    path('GuideTop/', views.GuideTopView.as_view(), name='guidetop'),
    path('TourSearch/', views.TourSearchView.as_view(), name='toursearch'),

    path("InformationPinChange/",views.InformationPinChangeView.as_view(),name="InformationPinChange"),
    path("InformationPinRegistration/",views.InformationPinRegistrationView.as_view(),name="InformationPinRegistration"),
    path("TourRegistration/",views.TourRegistrationView.as_view(),name="TourRegistration"),
    path("PasswordChange/",views.PasswordChangeView.as_view(),name="PasswordChange"),
]
# ---------------------------------------------------------
