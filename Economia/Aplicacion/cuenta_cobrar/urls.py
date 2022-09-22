from django.urls import path
from.views.menu.views import CobroTemplateView
from .views.cuenta.views import DetalleListView, CrearCuenta, CobroDeuda, EliminarView,DetalleListView2

app_name = "cuenta_cobrar"
urlpatterns = [
    path('menu',CobroTemplateView.as_view(), name="menu"),
    path('cobro', DetalleListView.as_view(), name="cobro"),
    path('crearcuenta/',CrearCuenta.as_view(), name="crearcuenta"),
    path('crear/', CobroDeuda.as_view(), name="crear"),
    path('eliminar/<int:pk>',EliminarView.as_view(),name="eliminar"),
    path('deuda',DetalleListView2.as_view(),name="deuda"),

]