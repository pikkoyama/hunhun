# あづーま
from django.urls import path, include
from . import views

app_name = 'tourists'

urlpatterns = [
    path(
        "tourmap/",
        views.TourmapView.as_view(),
        name="Tourmap"
    ),
    path(
        "languageselect/",
        views.LanguageSelectView.as_view(),
        name="LanguageSelect"
    ),
]
# -----------------------------------------------------/