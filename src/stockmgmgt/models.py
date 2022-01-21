from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stock(models.Model):
	nombre = models.CharField(max_length=50, blank=True, null=True)
	descripcion = models.CharField(max_length=50, blank=True, null=True)
	tipo = models.CharField(max_length=50, blank=True, null=True)
	serial = models.CharField(max_length=50, blank=True, null=True)
	valor_compra = models.IntegerField(default='0', blank=True, null=True)
	estado_actual = models.CharField(max_length=50, blank=True, null=True)
	persona_asignada = models.CharField(max_length=50, blank=True, null=True)
	fecha_compra = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.nombre