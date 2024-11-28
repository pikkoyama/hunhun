from django.shortcuts import render

# 小山 11/28--------------------------------
from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    template_name = 'index.html'

# ------------------------------------------/
