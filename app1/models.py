from django.db import models
from django.contrib.auth.models import User

LICENCIAS = (
		('CC','Creative Commons'),#opciones que podemos estar eligiendo
		('CCR','Compartir con creditos del creador'),
		('SL','Sin licencia'),
)

CATEGORIAS = (
			('LG','Logo'),
			('BR','Branding'),
			('ED','Editorial'),
			('PC','Packaging'),
			('AU','Audio Visual')


	)


class autorModel(models.Model):
	id = models.AutoField(primary_key=True)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	nombre_proyecto = models.CharField(max_length=50)
	nombre_empresa = models.CharField(max_length=50)
	descripcion = models.TextField(null=True, blank=True)
	tipo_licencia = models.CharField(choices = LICENCIAS,max_length=50, null=True, blank=True)
	categoria = models.CharField(choices = CATEGORIAS,max_length=50, null=True, blank=True)
 

def _str_(self): 
	return self.nombre_proyecto


# Create your models here.

