# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import messages
from appdelta.models import *
from appdelta.forms import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.template import RequestContext
from django.db.models import Q
# Create your views here.

class Viewindex(View):    
    
    template_name = 'index.html'
        
    def get(self, request, *args, **kwargs):
        if request.session['acceso'] == True:
            print(request.session['acceso'])
            Datos_cliente = datos_cliente.objects.all()
            
            query = request.GET.get('q', '')
            
            if query:
                qset = (
                    Q(name__icontains=query) |
                    Q(document__icontains=query) 
                )
                results = datos_cliente.objects.filter(qset).distinct()
            else:
                results = []
                
            return render(request, self.template_name, {
                "Datos_cliente": Datos_cliente,
                "results": results,
                "query": query
            })
        else:
            return HttpResponseRedirect(reverse('appdelta:login'))   


class Viewadmin(View):
    
    template_name = 'admin.html' 
    
    def get(self, request, *args, **kwargs):
        
        if request.session['acceso'] == True:
            Datos_cliente = datos_cliente.objects.all()
            query = request.GET.get('q', '')
            
            if query:
                qset = (
                    Q(name__icontains=query) |
                    Q(document__icontains=query) 
                )
                results = datos_cliente.objects.filter(qset).distinct()
            else:
                results = []            
            return render_to_response(self.template_name, {
                "Datos_cliente": Datos_cliente,
                "results": results,
                "query": query
            })
        else:
            return HttpResponseRedirect(reverse('appdelta:login'))
       
       
class Viewagregar(View):

    template_name = 'agregarclientes.html'     
        
    def get(self, request, *args, **kwargs): 
        if request.session['acceso'] == True:
            form = PostForm()
            return render(request, self.template_name, {
                    'form': form,
                })
        else:
            return HttpResponseRedirect(reverse('appdelta:login'))
         
    def post(self, request, *args, **kwargs):
        datos = datos_cliente.objects.all()
        form = PostForm(request.POST)
        
        if request.POST.get('save'):
                       
            if form.is_valid():
                
                appdelta = form.save(commit=False)
                appdelta.total_payment = (appdelta.percent/100) * appdelta.loan + appdelta.loan
                appdelta.deuda_actual = (appdelta.percent/100) * appdelta.loan + appdelta.loan
                appdelta.total_abonado = 0
                appdelta.presmaspor = 0
                appdelta.presmaspor = appdelta.loan + (appdelta.loan * appdelta.percent/100)
                
                appdelta.date = datetime.now().strftime("%Y/%m/%d")             
                
                appdelta.datelimite = datetime.now()+timedelta(days=appdelta.payment_days)
                appdelta.datelimite= appdelta.datelimite.strftime("%Y/%m/%d")
                
                appdelta.save()
                print('hola')
                return HttpResponseRedirect(reverse('appdelta:agregarclientes'))
            else:
                return render(request, self.template_name, {
                    'form': form,
            })


class Viewabono(View):
    
    template_name = 'abono.html'
    
    def get(self, request, *args, **kwargs):
        if request.session['acceso'] == True:
            Datos_cliente = datos_cliente.objects.get(pk=kwargs['pk'])
            form = AbonoForm(instance=Datos_cliente)
            return render(request, self.template_name, {
                'form': form,
            })
        else:
            return HttpResponseRedirect(reverse('appdelta:login'))
        
    def post(self, request, *args, **kwargs):
        Datos_cliente = datos_cliente.objects.get(pk=kwargs['pk']) 
        form = AbonoForm(request.POST, instance=Datos_cliente)
        
        if request.POST.get('saveabono'):
            if form.is_valid():
                Datos_cliente = form.save(commit=False)
                Datos_cliente.deuda_actual = Datos_cliente.deuda_actual - Datos_cliente.payment
                Datos_cliente.save()
                return HttpResponseRedirect(reverse('appdelta:index'))
            else:
                return render(request, self.template_name, {
                    'form': form,
    })


class Vieweditar(View):
    
    template_name = 'editarclientes.html'
    
    def get(self, request, *args, **kwargs):
        if request.session['acceso'] == True:
            Datos_cliente = datos_cliente.objects.get(pk=kwargs['pk'])
            form = EditForm(instance=Datos_cliente)
            return render(request, self.template_name, {
                'form': form,
            })
        else:
            return HttpResponseRedirect(reverse('appdelta:login'))
        
    def post(self, request, *args, **kwargs):
        Datos_cliente = datos_cliente.objects.get(pk=kwargs['pk']) 
        form = EditForm(request.POST, instance=Datos_cliente)
        
        if request.POST.get('saveedit'):
            if form.is_valid():
                Datos_cliente = form.save()
                return HttpResponseRedirect(reverse('appdelta:index'))
            else:
                return render(request, self.template_name, {
                    'form': form,
    })            
    
    
class Viewadcliente(View):
    
    template_name = 'admincliente.html'
    
    def get(self, request, *args, **kwargs):
        if request.session['acceso'] == True:
            datos = datos_cliente.objects.get(pk=kwargs['pk'])
            fecha = datetime.now().strftime("%Y/%m/%d")
            prestamo = prestamo_cliente.objects.all()
            form = AdminForm
            return render(request, self.template_name, {'form': form, 'datos': datos, })
        else:
            return HttpResponseRedirect(reverse('appdelta:login'))
    
    def post(self, request, *args, **kwargs):
        try:

            prestamo = prestamo_cliente.objects.all()
            abono_dia = 0
            fecha = datetime.now().strftime("%Y/%m/%d")
            datos = datos_cliente.objects.get(pk=kwargs['pk'])                      
            form = AdminForm(request.POST)
            if request.POST.get('savepres'):
                if form.is_valid():
                    appdelta = form.save(commit=False)
                    print(appdelta.total_payment)

                    if datos.total_payment == None:
                        datos.total_payment = 0
                    else:
                        datos.total_payment = datos.total_payment - appdelta.payment
                        appdelta.total_payment = datos.total_payment
                        print(datos.total_payment)

                    if datos.total_abonado == None:
                        datos.total_abonado = 0
                        datos.total_abonado = datos.total_abonado + appdelta.payment
                        appdelta.total_abonado = datos.total_abonado
                    else:
                        datos.total_abonado = datos.total_abonado + appdelta.payment
                        appdelta.total_abonado = datos.total_abonado                     
                    
                    if datos.presmaspor == None:
                        datos.presmaspor = 0
                        datos.presmaspor = datos.loan + (datos.loan * datos.percent/100)
                    
                    if datos.total_abonado == None:
                        datos.total_abonado = 0
                    
                    
                    appdelta.documen = datos
                    appdelta.date = datetime.now().strftime("%Y/%m/%d")
                    appdelta.hour = datetime.now().strftime("%H:%M")                
                    datos.save()
                    appdelta.save()
                    return HttpResponseRedirect(reverse('appdelta:admin'))            
                else:
                    return render(request, self.template_name, {'form': form, 'datos': datos,})            
        except ObjectDoesNotExist:
            raise Htpp404("No existe la cuenta")
        

class Viewmirar(View):
    
    template_name = 'verabonos.html'
    
    def get(self, request, *args, **kwargs):
        if request.session['acceso'] == True:
            prestamo = prestamo_cliente.objects.all().filter(documen = kwargs["pk"])        
            form = AbonoForm(request.GET)        
            return render(request, self.template_name, {
                'prestamo': prestamo,
            })
        else:
            return HttpResponseRedirect(reverse('appdelta:login'))
        

class Viewlogin(View):
    
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        login = login_admin.objects.all()
        form = LoginForm(request.GET)
        return render(request, self.template_name, {'form': form, 'login': login,})
    
    def post(self, request, *args, **kwargs):
        
        if request.POST.get('press'):
            
            form = LoginForm(request.POST)
            login = login_admin.objects.all()
            if form.is_valid(): 
                appdelta = form.save(commit=False)
                for log in login:
                    if log.customers == appdelta.customers and log.password == appdelta.password:                        
                        nombre_global = log.name
                        request.session['permisos'] = log.permisos
                        request.session['acceso'] = True
                        request.session['nombre'] = log.name
                        request.session['cargo'] = log.cargo
                        request.session['id'] = log.id
                        return HttpResponseRedirect(reverse('appdelta:inicio'))
                    else:                        
                        request.session['acceso'] = False
            else:
                return render(request, self.template_name, {'form': form, 'login': login,})
            

class Viewcerrar(View):
    
    template_name = 'cerrarseccion.html'
    
    def get(self, request, *args, **kwargs):
        if request.session['acceso'] == True:
            request.session['acceso'] = False
            return HttpResponseRedirect(reverse('appdelta:login'))
        else:
            request.session['acceso'] = False
            return HttpResponseRedirect(reverse('appdelta:login'))
     
        
class Viewinicio(View):
    
    template_name = 'inicio.html'
    
    def get(self, request, *args, **kwargs):
        user = request.session['nombre']
        cargo = request.session['cargo']
        id = request.session['id']
        if request.session['acceso'] == True:            
            return render(request, self.template_name, {'user': user, 'cargo': cargo, 'id': id })
        else:            
            return HttpResponseRedirect(reverse('appdelta:login'))
        

class Viewinformacion(View):
    
    template_name = 'informacion.html'
    
    def get(self, request, *args, **kwargs):
        
        prestamo = prestamo_cliente.objects.all()
        
        if request.session['acceso'] == True:
            total_usuarios = 0
            total_prestado = 0
            total_deuda = 0
            total_abono = 0
            prestadoiva = 0
            
            abono_dia = 0
            abono_dias = 0
            
            fecha = datetime.now().strftime("%Y/%m/%d")
            datos = datos_cliente.objects.all()            
            
            
            for dat in datos:
                total_abono = total_abono + dat.total_abonado
                total_prestado = total_prestado + dat.total_payment
                total_usuarios = total_usuarios + 1
                prestadoiva = prestadoiva + dat.presmaspor
            
            
            print ("prestado mas intereses " + repr(prestadoiva))
            print("total usuarios " + repr(total_usuarios))
            print("total prestado " + repr(total_prestado))
            print("total abonado " + repr(total_abono))
            print("abonado diario" + repr(abono_dia))
            prestamointe = request.session['prestamointe'] = prestadoiva
            usuarios = request.session['usuarios'] = total_usuarios
            prestado = request.session['prestado'] = total_prestado
            abonado = request.session['abonado'] = total_abono
            
            print("entro")   
                   
            query = request.GET.get('q', '')
            qset = (query)

            for prest in prestamo:                
                if prest.date == fecha:
                    abono_dia = abono_dia + prest.payment
                else:
                    if prest.date == qset:
                        fecha = qset
                        abono_dia = abono_dia + prest.payment
                
                #print("prueba" + repr(abono_dia))  
            
            return render(request, self.template_name, {'datos': datos, 'prestamointe': prestamointe, 'usuarios': usuarios, 'prestado': prestado, 'abonado': abonado, 
                                                        'abono_dia':abono_dia, 'fecha':fecha})
        else:                        
            return HttpResponseRedirect(reverse('appdelta:login'))
        


        

    
            
        

