from django.db import models

class ModeloPrimario(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta: # poder identificar una etiqueta que es la que identifica la aplicacion multi_app y la tabla en la BBDD
        app_label = 'multi_app'
        db_table = 'modelo_primario'

class ModeloSecundario(models.Model): 
    apellido = models.CharField(max_length=100)

    class Meta: # clase meta tambien se ocupa para anular migraciones por defecto de django
        app_label = 'multi_app'
        db_table = 'secondary'

# Create your models here.
