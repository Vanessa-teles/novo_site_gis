from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContatoForm

def index(request):
    return render(request, 'core/index.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            try:
                form.sendEmail()
                messages.success(request, 'E-mail enviado com sucesso!')
                return redirect(reverse('contato'))
            except Exception as e:
                messages.error(request, f'Erro ao enviar e-mail: {str(e)}')
                return redirect(reverse('contato'))
    return render(request, 'core/contato.html')

from django.core.mail import send_mail, EmailMessage