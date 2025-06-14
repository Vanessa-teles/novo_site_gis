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
                # Chamando o método send_email (não send_mail)
                form.send_email()
                return redirect('pagina_de_sucesso')  # Redireciona após envio
            except Exception as e:
                # Adiciona erro ao formulário para mostrar ao usuário
                form.add_error(None, f'Erro ao enviar mensagem: {str(e)}')
    else:
        form = ContatoForm()
    
    return render(request, 'seu_template.html', {'form': form})

from django.core.mail import send_mail, EmailMessage