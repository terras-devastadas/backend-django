from django import forms
from .models import Comunidade

class ComunidadeForm(forms.ModelForm):
    class Meta:
        model = Comunidade
        fields = ['nome', 'descricao', 'banner', 'visibilidade_alunos', 'visibilidade_professores']
