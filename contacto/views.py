from django.shortcuts import render, redirect
from .forms import FormularioContacto
import smtplib
from django.core.mail import EmailMessage,send_mail
from ProyectoWeb.settings import EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

# Create your views here.

def contacto(request):
    
    formulario = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(request.POST) #llenar info del formulario con la data del request.post

        if formulario_contacto.is_valid(): # si el formulario_contacto es valido (se ha rellenado los campos)

            formulario_contacto.cleaned_data

            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App django","nombre: {}\nDireccion:{}\nEmail: {}".format(nombre,email,contenido)
            ,"",['qntumforce@gmail.com'],reply_to=[email])


        try: 
            ''' send_mail('Contacto App django', 'contenido: {}'.format(
                contenido), email, ['qntumforce@gmail.com'],) '''

            email.send()

            return redirect("/contacto/?valido")

        except:
            return redirect("/contacto/?novalido")


    return render(request,"contacto/contacto.html",{'formulario':formulario})
