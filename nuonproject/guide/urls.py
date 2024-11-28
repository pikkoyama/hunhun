# 小山 11/28-------------------------------------------
from django.urls import path
from . import views

app_name = 'guide'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
# -----------------------------------------------------/