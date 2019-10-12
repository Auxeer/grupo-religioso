from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Actividad, Participantes_Actividad, Persona, Comunidad

from django.forms import SelectDateWidget
from django.utils import timezone

# ------------------------------------

class ActividadForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super(ActividadForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Actividad
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }

# ------------------------------------

class PersonaForm(ModelForm):
    comunidad = forms.ModelChoiceField(queryset=Comunidad.objects.all(),empty_label="Seleccione una Comunidad")

    def __init__(self, *args, **kwargs):
            super(PersonaForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
                'nombre_persona': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            }

# ------------------------------------

class ComunidadForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super(ComunidadForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Comunidad
        fields = '__all__'
    
# ------------------------------------

class PartActForm(ModelForm):
    persona = forms.ModelChoiceField(queryset=Persona.objects.all(),empty_label="Seleccione un Participante")

    def __init__(self, *args, **kwargs):
            super(PartActForm, self).__init__(*args, **kwargs)
            self.fields['persona'].widget.attrs\
            .update({
                'class': 'form-control'
            })

    class Meta:
        model = Participantes_Actividad
        exclude = ()

PartActFormSet = inlineformset_factory(Actividad, Participantes_Actividad, form=PartActForm, extra=3, can_delete=True)

# ------------------------------------