from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _

class ContatoForm(forms.Form):
    nome = forms.CharField(label=_("Nome"), max_length=100)
    email = forms.EmailField(label=_("Email"), max_length=100)
    assunto = forms.CharField(label=_("Assunto"), max_length=100)
    mensagem = forms.CharField(label=_("Descreva sua necessidade"), widget=forms.Textarea())
    telefone = forms.CharField(label=_("Telefone"), max_length=15)
    cidade = forms.CharField(label=_("Endereço do imóvel"), max_length=100)
    service = forms.CharField(label=_("Serviço"), max_length=100)

    SERVICE_CHOICES_MAP = {
        "entrega": "Vistoria de Entrega de Chaves",
        "sindico": "Vistoria para Síndicos",
        "laudo": "Laudos Técnicos",
        "outro": "Outro serviço",
    }

    def send_mail(self):
        """Método para enviar e-mail com tratamento completo"""
        try:
            # Coleta de dados
            nome = self.cleaned_data["nome"]
            email = self.cleaned_data["email"]
            assunto = self.cleaned_data["assunto"]
            mensagem = self.cleaned_data["mensagem"]
            cidade = self.cleaned_data["cidade"]
            telefone = self.cleaned_data["telefone"]
            service_value = self.cleaned_data["service"]
            
            service_full_text = self.SERVICE_CHOICES_MAP.get(service_value, service_value)

            # Corpo do e-mail formatado
            conteudo = f"""
            NOVO CONTATO - {assunto}
            Nome: {nome}
            E-mail: {email}
            Telefone: {telefone}
            Cidade: {cidade}
            Serviço: {service_full_text}
            Mensagem:
            {mensagem}
            """

            # Envio usando send_mail (que funcionou no shell)
            result = send_mail(
                subject=f"Contato do Site: {assunto}",
                message=conteudo,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_DESTINO],
                fail_silently=False
            )
            
            # Retorna True se o e-mail foi enviado com sucesso
            return result == 1
            
        except Exception as e:
            print(f"ERRO NO ENVIO: {str(e)}")  # Log para debug
            return False