from django.urls import path
from . import views
# from .views import get_pins

app_name = 'tourists'

urlpatterns = [
    path('tourmap/', 
         views.TourmapView.as_view(), 
         name='Tourmap'
         ),

    path('languageselect/', 
         views.LanguageSelectView.as_view(), 
         name='LanguageSelect'
         ),

    path('api/pins/', 
         views.get_pins, 
         name='get_pins'
         ),
]