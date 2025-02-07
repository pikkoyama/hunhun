# 清原 1/8-------------------------------------------
from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    # トップページ画面(管理者専用)
    path(
        "admintop/",
        views.AdminTopView.as_view(),
        name="AdminTop"
    ),
    # 
    path(
        "adminview/",
        views.AdminViewView.as_view(),
        name="AdminViewAccount"
    ),
    # アカウント作成URL
    path(
        "admincreate/",
        views.AdminCreateView.as_view(),
        name="AdminCreateAccount"
    ),
    # 
    path(
        "adminsuccess/",
        views.AdminSuccessView.as_view(),
        name="AdminTransmissionComp"
    ),
    # 事例削除URL
    path(
        "casedelete/",
        views.CaseDeleteView.as_view(),
        name="CaseDelete"
    ),
    #アカウント削除URL
    path(
        "accountdelete/",
        views.AccountDeleteView.as_view(),
        name="AccountDelete"
    ),
# 根岸
    path('guides/', views.guide_account_list, name='guide_account_list'),
    path('guides/delete/<int:guide_id>/', views.delete_guide_account, name='delete_guide_account')

    
]
# -----------------------------------------------------/