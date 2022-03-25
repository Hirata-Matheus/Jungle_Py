#rodar esse script pra download: pip install django-bootstrap4 django-stdimage
from dataclasses import fields
from email.message import EmailMessage
from django import forms
from django.core.mail.message import EmailMessage
from .models import Pessoa

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='E-Mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=50)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)
    
    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage(
            subject='E-Mail enviado pelo Django',
            body=conteudo,
            from_email='no-reply@hirata.com.br',
            to = ['matheushirata2001@outlook.com'],
            headers={'Reply-to': email})
        mail.send()
        
class PessoaModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['Codigo', 'Nome', 'Email', 'Telefone', 'Dtanas']