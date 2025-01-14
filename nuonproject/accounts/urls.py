# 小山 1/7-------------------------------------------
from django.urls import path
from . import views
from manager.views import admin_dashboardView,homeView

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
    path('admin_dashboard/', admin_dashboardView.as_view(), name='admin_dashboard'),  # 管理者用ダッシュボードのURL
    path('home/', homeView.as_view(), name='home'),
]
# -----------------------------------------------------/