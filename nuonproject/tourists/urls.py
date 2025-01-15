from django.urls import path
from . import views

app_name = 'tourists'

urlpatterns = [
    path("tourmap/", 
         views.TourmapView.as_view(), 
         name="Tourmap"
         ),

    path("languageselect/", 
         views.LanguageSelectView.as_view(), 
         name="LanguageSelect"
         ),
]