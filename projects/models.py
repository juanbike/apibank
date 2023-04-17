from django.db import models

# Create your models here.

#
#==============================================================
#			CTACONTAB	Char(20)	Cuenta Contable Completa 20 Digitos
#							Ejemplo: 13136101000100000000
#			AGENCIA	Char(4)	Código de Agencia Ejemplo: “0001”
#			MONEDA	Char(3)	Código de Moneda: Ejemplo: “VES”
#			FECHASTA	Char(8)	DDMMAAAA: 20112022
#========================================================
#

class cuentaContable(models.Model):
    ctaContable = models.CharField(max_length=20),
    agencia = models.CharField(max_length=4)
    moneda = models.CharField(max_length=3)
    fechaHasta = models.CharField(max_length=8)   