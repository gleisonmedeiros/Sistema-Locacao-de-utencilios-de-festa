from django import forms
from .models import Produto_Model, Cliente_Model, PedidoModel, ItemPedido

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto_Model
        fields = '__all__'
        dicionario = {'class': 'form-control', 'type': 'text'}
        widgets = {
            'nome': forms.TextInput(attrs=dicionario),
            'modelo': forms.TextInput(attrs=dicionario),
            'quantidade': forms.TextInput(attrs=dicionario),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente_Model
        fields = '__all__'
        dicionario = {'class': 'form-control', 'type': 'text','id':'','placeholder': ''}
        widgets = {
            'nome': forms.TextInput(attrs=dicionario),
            'telefone':forms.TextInput(attrs={**dicionario,'placeholder':'(00) 00000 - 0000','id':'tel'}),
            'cep': forms.TextInput(attrs={**dicionario, 'placeholder': '00000 - 000','id':'cep'}),
            'estado': forms.TextInput(attrs={**dicionario,'id': 'inputestado'}),
            'cidade': forms.TextInput(attrs={**dicionario,'id': 'inputcidade'}),
            'endereco': forms.TextInput(attrs={**dicionario,'id': 'inputendereco'}),
            'numero': forms.TextInput(attrs={**dicionario,'id': 'inputnumero'}),
            'referencia': forms.TextInput(attrs={**dicionario,'id': 'inputref'}),
        }
        labels = {
            'endereco': 'Endereço',
            'numero':'Número',
            'referencia':'Ponto de Referência'
        }


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade_alugada']

class PedidoModelForm(forms.ModelForm):
    class Meta:
        dicionario = {'class': 'form-select', 'aria-label':'Default select example'}
        dicionario2 = {'class': 'form-control', 'type': 'text', 'id': '', 'placeholder': ''}
        model = PedidoModel
        fields = ['cliente', 'data_de_locacao','local','observacao']
        widgets = {
            'cliente': forms.Select(attrs=dicionario),
            'data_de_locacao': forms.TextInput(attrs={**dicionario,'id': 'id_data','type': 'date'}),
            'local': forms.TextInput(attrs=dicionario2),
            'observacao': forms.TextInput(attrs=dicionario2),
        }

    itens_pedido = forms.inlineformset_factory(
        PedidoModel,
        ItemPedido,
        form=ItemPedidoForm,
        fields=['produto', 'quantidade_alugada'],
        extra=1,
        can_delete=True,
        widgets={
            'produto': forms.Select(attrs={'class': 'form-select', 'aria-label': 'Produto'}),
            'quantidade_alugada': forms.NumberInput(
                attrs={'class': 'form-control'}),
        },
    )

class DateRangeForm(forms.Form):
    data_inicio = forms.DateField(label='Data de Início', widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}))
    data_fim = forms.DateField(label='Data de Fim', widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}))