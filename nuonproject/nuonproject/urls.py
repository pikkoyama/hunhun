"""
URL configuration for nuonproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views

# 小山
from django.conf import settings
from django.conf.urls.static import static

app_name = 'guidesupport'

urlpatterns = [
    path('admin/', admin.site.urls),

    # guideのパス
    path('guide/', include('guide.urls')),
# 1/7 小山
    # accountsのパス
    path('accounts/',include('accounts.urls')),
# 直接サインインページに行くためのパス
    path('', views.SinInView.as_view(), name='sinin'),
# 1/8 あづ
    path('tourists/',include('tourists.urls')),

    path('manager/',include('manager.urls'))
]
# 小山
# urlpatterns にmediaフォルダのURLパターンを追加（P467）
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
