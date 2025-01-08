from django.shortcuts import render

# 我妻1/8--------------------------------
from django.views.generic.base import TemplateView

class TourmapView(TemplateView):
    # ねぎしま
    template_name = "Tourmap.html"

class LanguageSelectView(TemplateView):
    # ねぎしまさ
    template_name = "LanguageSelect.html"
# ------------------------------------------/
