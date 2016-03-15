from django.db import models
from datetime import date

# Create your models here.
class datos_cliente(models.Model):
    
    name = models.CharField('Nombre', max_length=200, null=True, db_column='name')   
    date = models.CharField('Fecha', max_length=100, null=True, db_column='date')
    dateprestamo = models.CharField('Fecha del prestamo', max_length=100, null=True, db_column='dateprestamo')
    document = models.CharField('Documento', max_length=50, db_column='document', primary_key=True)
    Address = models.CharField('Direcion', max_length=200, null=True, db_column='Address')
    trade = models.CharField('Negocio', max_length=50, null=True, db_column='trade')
    loan = models.IntegerField('Prestamo', null=True, db_column='loan')
    percent = models.IntegerField('Porcentaje', null=True, db_column='percent')
    payment_days = models.IntegerField('Dias a pagar', null=True, db_column='payment_days')
    phone = models.CharField('Telefono', max_length=50, null=True, db_column='phone')
    total_payment = models.IntegerField('Total a pagar', null=True, db_column='total_payment')
    total_abonado = models.IntegerField('Total abonado', null=True, db_column='total_abonado')
    presmaspor = models.IntegerField('Prestamos mas porcentaje', null=True, db_column='presmaspor')
    datelimite = models.CharField('Fecha limite del pago', max_length=100, null=True, db_column='datelimite')
    

class prestamo_cliente(models.Model):
    
    documen = models.ForeignKey(datos_cliente, verbose_name='Documento')
    date = models.CharField('Fecha', max_length=100, null=True, db_column='date')
    hour = models.CharField('Hora', max_length=100, null=True, db_column='hour')
    total_payment = models.IntegerField('Total a pagar', null=True, db_column='total_payment') 
    payment = models.IntegerField('Abono', null=True, db_column='payment')
    total_abonado = models.IntegerField('Total abonado', null=True, db_column='total_abonado')
    total_abonado_dia = models.IntegerField('Total abonado dia', null=True, db_column='total_abonado_dia')
    
    
class informacion_general(models.Model):    
    
    total_debt = models.CharField('Deuda total', max_length=100, null=True, db_column='total_debt')
    date = models.CharField('Fecha', max_length=100, null=True, db_column='date') 
    total_customers = models.CharField('Total clientes', max_length=100, null=True, db_column='total_customers')
    total_collect_day = models.CharField('Total recaudado en el dia', max_length=100, null=True, db_column='total_collect_day')
    
    
class login_admin(models.Model):
    
    name = models.CharField('Nombre', max_length=200, null=True, db_column='name')
    customers = models.CharField('Usuario', max_length=200, null=True, db_column='customers')
    password = models.CharField('Contrasena', max_length=200, null=True, db_column='password')
    passw = models.CharField('Contrasena', max_length=200, null=True, db_column='passw')
    permisos = models.IntegerField('Permisos', null=True, db_column='permisos')
    cargo = models.CharField('Cargo', max_length=200, null=True, db_column='cargo')
    
    
class informacion_diaria(models.Model):
    date = models.CharField('Fecha', max_length=100, null=True, db_column='date')
    abono_diario = models.CharField('Abono diario', max_length=200, null=True, db_column='abono_diario')