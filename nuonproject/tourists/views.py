from django.views.generic import TemplateView

class LanguageSelectView(TemplateView):
    template_name = 'LanguageSelect.html'

class TourmapView(TemplateView):
    template_name = 'Tourmap.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = self.request.GET.get('language', 'ja')
        return context