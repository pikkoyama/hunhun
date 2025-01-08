from django.shortcuts import render

# 清原 1/8--------------------------------
from django.views.generic.base import TemplateView

class AdminTopView(TemplateView):

    template_name = 'AdminTop.html'

# ------------------------------------------/
