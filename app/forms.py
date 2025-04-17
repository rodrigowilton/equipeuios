# app/forms.py

from django import forms
from .models import AppBanco

class MessageForm(forms.Form):
    contacts = forms.ModelMultipleChoiceField(queryset=AppBanco.objects.all())
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)


class AppBancoForm(forms.ModelForm):
    class Meta:
        model = AppBanco
        fields = ['nome', 'celular', 'cep', 'endereco', 'complemento', 'bairro', 'localidade', 'uf', 'numero', 'aceita_whatsapp', 'nome_lider', 'insta']
        widgets = {
            'cep': forms.TextInput(attrs={'id': 'id_cep'}),
            'endereco': forms.TextInput(attrs={'id': 'id_endereco'}),
            'complemento': forms.TextInput(attrs={'id': 'id_complemento'}),
            'bairro': forms.TextInput(attrs={'id': 'id_bairro'}),
            'localidade': forms.TextInput(attrs={'id': 'id_localidade'}),
            'uf': forms.TextInput(attrs={'id': 'id_uf'}),
            'numero': forms.TextInput(attrs={'id': 'id_numero'}),
            'aceita_whatsapp': forms.Select(choices=AppBanco._meta.get_field('aceita_whatsapp').choices, attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opcional: Adicionar um label mais amigável ao dropdown
        self.fields['aceita_whatsapp'].label = "Aceita receber mensagem pelo WhatsApp?"