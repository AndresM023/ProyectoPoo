from django.db import models
from django.utils import timezone
# Create your models here.

meses_diferidos = [
    ('3 meses','3 meses'),('6 meses','6 meses'),('9 meses','9 meses'),('12 meses','12 meses'),('24 meses','24 meses')
]


class Cabecera(models.Model):
    nombre= models.CharField(max_length=200, unique=True)
    deuda = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto a diferir')
    fecha_cobro = models.DateField(blank=True, null=True)
    meses_a_diferir = models.CharField(max_length=200,choices=meses_diferidos,default=meses_diferidos[0][0])
    cuota_mensual = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='Cuota Mensual',default=0.00)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = "Cabecera"
        verbose_name_plural = "Cabeceras"
        ordering = ('nombre',)


class PagoDeuda(models.Model):
    abono = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Pago')
    fecha_ab = models.DateField('Fecha de pago',default=timezone.now)
    deuda = models.ForeignKey(Cabecera,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return "{}".format(self.abono,self.deuda.deuda)

    class Meta:
        pass


