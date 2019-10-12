from django.contrib import admin
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

# Register your models here.
from .models import Comunidad
from .models import Persona
from .models import Actividad, Participantes_Actividad

admin.site.register(Comunidad)
admin.site.register(Persona)

class Participantes_ActividadInline(admin.TabularInline):
    model = Participantes_Actividad

class ActividadAdmin(admin.ModelAdmin):
    inlines = (Participantes_ActividadInline,)

admin.site.register(Actividad, ActividadAdmin)