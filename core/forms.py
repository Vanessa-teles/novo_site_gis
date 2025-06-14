from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _

class ContatoForm(forms.Form):
    nome = forms.CharField(label=_('Nome'), max_length=100)
    email = forms.EmailField(label=_('Email'), max_length=100)
    assunto = forms.CharField(label=_('Assunto'), max_length=100)
    mensagem = forms.CharField(label=_('Mensagem'), widget=forms.Textarea())
    telefone = forms.CharField(label=_('Telefone'), max_length=15)
    cidade = forms.CharField(label=_('cidade'), max_length=100)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        cidade = self.cleaned_data['cidade']
        telefone = self.cleaned_data['telefone']

        n = _(nome)
        e = _(email)
        a = _(assunto)
        m = _(mensagem)
        c = _(cidade)
        t = _(telefone)

        conteudo = f'NOVO CONTATO VIA E-MAIL\nNome do Cliente: {n}\nEmail informado para contato: {e}\nCidade: {c}\nTelefone informado para contato: {t}\nAssunto: {a}\nMensagem: {m}\n'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='gislaine.teles.eng@gmail.com',
            to=['gislaine_teles@outlook.com',],
            headers={'Reply-To': email}
        )
        mail.send()
