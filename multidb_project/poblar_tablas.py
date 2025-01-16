import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multidb_project.settings') 
django.setup()

from multi_app.models import ModeloPrimario, ModeloSecundario


def poblar_modelos():
    # Poblar la tabla ModeloPrimario (PostgreSQL)
    datos_primarios = ['Juan', 'Ana', 'Carlos', 'María', 'Luis']
    for nombre in datos_primarios:
        ModeloPrimario.objects.create(nombre=nombre)
    print(f'{len(datos_primarios)} registros añadidos a "modelo_primario" en PostgreSQL.')

    # Poblar la tabla ModeloSecundario (MySQL)
    datos_secundarios = ['Pérez', 'García', 'López', 'Martínez', 'Sánchez']
    for apellido in datos_secundarios:
        ModeloSecundario.objects.create(apellido=apellido)
    print(f'{len(datos_secundarios)} registros añadidos a "secondary" en MySQL.')


if __name__ == '__main__':
    poblar_modelos()