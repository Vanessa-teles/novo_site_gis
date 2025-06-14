from django.shortcuts import render, redirect
from .forms import ContatoForm

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            if form.send_email():
                return redirect('contato_sucesso')
            else:
                form.add_error(None, "Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente mais tarde.")
    else:
        form = ContatoForm()
    
    return render(request, 'contato.html', {'form': form})