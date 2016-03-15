from django import forms
from .models import datos_cliente
from .models import prestamo_cliente
from .models import login_admin

class PostForm(forms.ModelForm):

        class Meta:
            
            model = datos_cliente
            exclude = ['total_payment','deuda_actual','payment','total_abonado','date','presmaspor','dateprestamo','datelimite']

            widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'document': forms.TextInput(attrs={'class': 'form-control'}),
                'Address': forms.TextInput(attrs={'class': 'form-control'}),
                'trade': forms.TextInput(attrs={'class': 'form-control'}),
                'loan': forms.TextInput(attrs={'class': 'form-control'}),
                'payment_days': forms.TextInput(attrs={'class': 'form-control'}),
                'percent': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Porcentaje'}),
                'phone': forms.TextInput(attrs={'class': 'form-control'}),                
                'total_payment': forms.TextInput(attrs={'class': 'form-control'}),
                'deuda_actual': forms.TextInput(attrs={'class': 'form-control'}),
            }


class AdminForm(forms.ModelForm):
    
        class Meta:
            
            model = prestamo_cliente
            exclude = ['documen','sumado','deuda_actual','payment_total','date','total_payment','total_abonado','hour','total_abonado_dia','dateprestamo','datelimite']
            
            widgets = {
               'date': forms.TextInput(attrs={'class': 'form-control'}),               
               'total_days': forms.TextInput(attrs={'class': 'form-control'}),
               'total_payment': forms.TextInput(attrs={'class': 'form-control'}),
               'delayed_days': forms.TextInput(attrs={'class': 'form-control'}),
               'payment': forms.TextInput(attrs={'class': 'form-control'}),
               'sumado': forms.TextInput(attrs={'class': 'form-control'}),
               'deuda_actual': forms.TextInput(attrs={'class': 'form-control'}),
            }
            
            
class AbonoForm(forms.ModelForm):
    
        class Meta:
            
            model = datos_cliente
            exclude = ['trade','name','Address','loan','payment_days','percent','phone','total_payment','deuda_actual','payment_total','hour','total_abonado_dia',]
            
            widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'document': forms.TextInput(attrs={'class': 'form-control'}),
                'payment': forms.TextInput(attrs={'class': 'form-control'}),
                #'payment_total': forms.TextInput(attrs={'class': 'form-control'}),
            }
            
            
class EditForm(forms.ModelForm):
    
    class Meta:
            
            model = datos_cliente
            exclude = ['total_payment','deuda_actual','payment','document','loan','percent','payment_days','total_abonado','date','presmaspor','dateprestamo','datelimite']
    
            widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'Address': forms.TextInput(attrs={'class': 'form-control'}),
                'trade': forms.TextInput(attrs={'class': 'form-control'}),
                'phone': forms.TextInput(attrs={'class': 'form-control'}),
                'dateprestamo': forms.TextInput(attrs={'class': 'form-control'}), 
            }


class LoginForm(forms.ModelForm):
    
    class Meta:
            
            model = login_admin
            exclude = ['name','permisos','cargo','passw']
    
            widgets = {
                'customers': forms.TextInput(attrs={'class': 'form-control'}),
                'password': forms.TextInput(attrs={'class': 'form-control', 'type':'password'}),             
            }

           
class PasswForm(forms.ModelForm):
    
    class Meta:
            
            model = login_admin
            exclude = ['name','permisos','cargo','customers']
    
            widgets = {
                'password': forms.TextInput(attrs={'class': 'form-control', 'type':'password'}),             
            }
            
            
class DiaForm(forms.ModelForm):
    
    class Meta:
            
            model = login_admin
            exclude = ['date','abono_diario']
    
            widgets = {}

