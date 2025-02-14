#  1/7-------------------------------------------
from django.urls import path
from . import views
from manager.views import admin_dashboardView
from guide.views import homeView
from .views import CustomLogoutView,PasswordResetDoneView,PasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path(
        "sinin/",
        views.SinInView.as_view(),
        name="Sinin"
    ),
    path(
        "passworddone/",
        views.PasswordDoneView.as_view(),
        name="PasswordDone"
    ),
    path(
        "passwordemail/",
        views.PasswordEmailView.as_view(),
        name="PasswordEmail"
    ),
    path('password_reset_done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('admin_dashboard/', admin_dashboardView.as_view(), name='admin_dashboard'),  # 管理者用ダッシュボードのURL
    path('home/', homeView.as_view(), name='home'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
]
# -----------------------------------------------------/