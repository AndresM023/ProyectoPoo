from django.db import models
from django.utils import timezone
# Create your models here.


class Cabecera(models.Model):
    nombre= models.CharField(max_length=200, unique=True)
    deuda = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto a diferir')
    fecha_cobro = models.DateField(blank=False, null=False,default=timezone.now)
    meses_a_diferir = models.IntegerField(blank=False, null=False)
    cuota_mensual = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='Cuota Mensual',default=0.00)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Cabecera"
        verbose_name_plural = "Cabeceras"
        ordering = ('nombre',)



class PagoDeuda(models.Model):
    cabecera = models.ForeignKey(Cabecera, on_delete=models.CASCADE, null=True, blank=True,verbose_name='Cliente')
    abono = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Pago')
    fecha_ab = models.DateField('Fecha de pago',default=timezone.now,null = False,blank = False)



    def __str__(self):
        return "{} - {}".format(self.abono,self.cabecera)

    class Meta:
        pass


