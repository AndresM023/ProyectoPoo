from django.views.generic import TemplateView


class CobroTemplateView(TemplateView):
    template_name = 'main_cobro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cuenta_Cobrar"
        context['url_anterior'] = '/'
        return context

