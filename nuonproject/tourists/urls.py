# あづーま
from django.urls import path, include
from . import views

app_name = 'tourists'

urlpatterns = [
    path(
        "Tourmap/",
        views.TourmapView.as_view(),
        name="Tourmap"
    ),
    path(
        "LanguageSelect/",
        views.LanguageSelectView.as_view(),
        name="LanguageSelect"
    ),
]
# -----------------------------------------------------/