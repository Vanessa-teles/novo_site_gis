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
        """Método CORRETO para enviar e-mail"""
        nome = self.cleaned_data["nome"]
        email = self.cleaned_data["email"]
        assunto = self.cleaned_data["assunto"]
        mensagem = self.cleaned_data["mensagem"]
        cidade = self.cleaned_data["cidade"]
        telefone = self.cleaned_data["telefone"]
        service_value = self.cleaned_data["service"]
        
        service_full_text = self.SERVICE_CHOICES_MAP.get(service_value, service_value)

        conteudo = f"""
        NOVO CONTATO VIA E-MAIL
        Nome do Cliente: {nome}
        Email informado para contato: {email}
        Cidade: {cidade}
        Telefone informado para contato: {telefone}
        Serviço solicitado: {service_full_text}
        Assunto: {assunto}
        Mensagem: {mensagem}
        """

        mail = EmailMessage(
            subject=f"Novo contato: {assunto}",
            body=conteudo,
            from_email="gislaine.teles.eng@gmail.com", # Considere mover para settings.py
            to=["gislaine_teles@outlook.com"], # Considere mover para settings.py
            headers={"Reply-To": email}
        )
        mail.send()

        # NÃO coloque return ou print aqui fora da classe/função
        # O print abaixo está fora do método e com indentação incorreta, será ignorado.
        # Se for para debug, mova para dentro do método com indentação correta.
        # print("Mensagem enviada")