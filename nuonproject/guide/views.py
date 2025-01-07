from django.shortcuts import render

# 小山 11/28--------------------------------
from django.views.generic.base import TemplateView

class CaseListView(TemplateView):

    template_name = 'CaseList.html'

# ------------------------------------------/
    
class CaseRegistrationView(TemplateView):

    template_name = 'CaseRegistration.html'


class ExampleViewView(TemplateView):

    template_name = 'ExampleView.html'

class GuidancePinDeleteView(TemplateView):

    template_name = 'GuidancePinDelete.html'

class GuideTopView(TemplateView):

    template_name = 'GuideTop.html'

class TourSearchView(TemplateView):

    template_name = 'TourSearch.html'
