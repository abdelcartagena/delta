from django.contrib import admin
from django.contrib import admin
from .models import datos_cliente, prestamo_cliente, informacion_general

# Register your models here.

admin.site.register(datos_cliente)
admin.site.register(prestamo_cliente)
admin.site.register(informacion_general)