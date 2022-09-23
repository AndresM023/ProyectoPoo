from django.urls import reverse_lazy
from django.views.generic import DeleteView,ListView,CreateView
from Aplicacion.cuenta_cobrar.models import Cabecera,PagoDeuda
from Aplicacion.cuenta_cobrar.forms import CabeceraForm,PagoDeudaForm


class DetalleListView(ListView):
    template_name = "cobro.html"
    context_object_name = 'cobro'
    model = Cabecera


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/'
        context['listar_url'] = '/menu'
        context['titulo'] = 'Cuentas por Cobrar'
        context['registro'] = PagoDeuda.objects.filter()
        return context


class CrearCuenta(CreateView):
    model = Cabecera
    template_name = "parte/form.html"
    success_url = reverse_lazy('cuenta_cobrar:cobro')
    form_class = CabeceraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/cuenta_cobrar/crearcuenta/'
        context['titulo'] = 'Crear Registro'
        context['url_anterior'] = '/cuenta_cobrar/cobro'
        context['listar_url'] = '/cuenta_cobrar/cobro'
        return context




class CobroDeuda(CreateView):
    model = PagoDeuda
    form_class = PagoDeudaForm
    template_name = "parte/cobro_deuda.html"
    success_url = reverse_lazy('cuenta_cobrar:cobro')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/cuenta_cobrar/crear/'
        context['titulo'] = 'Sección para realizar el pago'
        context['url_anterior'] = '/cuenta_cobrar/cobro'
        context['listar_url'] = '/cuenta_cobrar/cobro'
        return context




class EliminarView(DeleteView):
    model = Cabecera
    template_name = "parte/eliminar.html"
    success_url = reverse_lazy('cuenta_cobrar:cobro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registros'
        context['url_anterior'] = '/cuenta_cobrar/cobro'
        context['listar_url'] = '/cuenta_cobrar/cobro/'
        return context






