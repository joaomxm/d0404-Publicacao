from django import forms 
from catalogo.models import Filme

class Adicionar_filme(forms.ModelForm):
    # cartaz = forms.ImageField(verbose_name='cartaz', upload_to='', required = False)
    class Meta:
        model= Filme
        fields=[

            'nome',
            'genero',
            'sinopse',
            'lancamento', 
            'duracao',
            'classificacao_indicativa', 
            'cartaz',
        ]