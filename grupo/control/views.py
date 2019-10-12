from django.shortcuts import render

# Create your views here.
from .models import Persona, Comunidad, Actividad

def index(request):
    return render(request, 'control/dashboard.html')


# def personas(request):
#    return render(request, 'control/persona/listar.html')

    
from django.views import generic

class PersonaListView(generic.ListView):
    model = Persona
    paginate_by = 10

class PersonaDetailView(generic.DetailView):
    model = Persona

# ------------------------------------

class ComunidadListView(generic.ListView):
    model = Comunidad
    paginate_by = 10

class ComunidadDetailView(generic.DetailView):
    model = Comunidad

# ------------------------------------

class ActividadListView(generic.ListView):
    model = Actividad
    paginate_by = 10

class ActividadDetailView(generic.DetailView):
    model = Actividad

# ------------------------------------

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Persona, Comunidad, Actividad, Participantes_Actividad

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from .forms import *

class PersonaCreate(CreateView):
    model = Persona
    # fields = '__all__'
    form_class = PersonaForm
    success_url = reverse_lazy('control:personas')
    template_name_suffix = '_crear'

    @method_decorator(permission_required('control.add_persona',reverse_lazy('control:personas')))
    def dispatch(self, *args, **kwargs):
            return super(PersonaCreate, self).dispatch(*args, **kwargs)

class PersonaUpdate(UpdateView):
    model = Persona
    # fields = ['nombre_persona','apellido','edad','comunidad']
    form_class = PersonaForm
    template_name_suffix = '_crear'

    @method_decorator(permission_required('control.change_persona',reverse_lazy('control:personas')))
    def dispatch(self, *args, **kwargs):
            return super(PersonaUpdate, self).dispatch(*args, **kwargs)

class PersonaDelete(DeleteView):
    model = Persona
    success_url = reverse_lazy('control:personas')
    template_name_suffix = '_eliminar'

    @method_decorator(permission_required('control.delete_persona',reverse_lazy('control:personas')))
    def dispatch(self, *args, **kwargs):
            return super(PersonaDelete, self).dispatch(*args, **kwargs)

# ------------------------------------

class ComunidadCreate(CreateView):
    model = Comunidad
    # fields = '__all__'
    form_class = ComunidadForm
    success_url = reverse_lazy('control:comunidades')
    template_name_suffix = '_crear'

    @method_decorator(permission_required('control.add_persona',reverse_lazy('control:comunidades')))
    def dispatch(self, *args, **kwargs):
            return super(ComunidadCreate, self).dispatch(*args, **kwargs)

class ComunidadUpdate(UpdateView):
    model = Comunidad
    # fields = ['nombre_comunidad','departamento','municipio']
    form_class = ComunidadForm
    success_url = reverse_lazy('control:comunidades')
    template_name_suffix = '_crear'

    @method_decorator(permission_required('control.change_persona',reverse_lazy('control:comunidades')))
    def dispatch(self, *args, **kwargs):
            return super(ComunidadUpdate, self).dispatch(*args, **kwargs)

class ComunidadDelete(DeleteView):
    model = Comunidad
    success_url = reverse_lazy('control:comunidades')
    template_name_suffix = '_eliminar'

    @method_decorator(permission_required('control.delete_persona',reverse_lazy('control:comunidades')))
    def dispatch(self, *args, **kwargs):
            return super(ComunidadDelete, self).dispatch(*args, **kwargs)

# ------------------------------------

class ActividadCreate(CreateView):
    model = Actividad
    # fields = '__all__'
    form_class = ActividadForm
    success_url = reverse_lazy('control:actividades')
    template_name_suffix = '_crear'

    def get_context_data(self, **kwargs):
        context = super(ActividadCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['actividadespar'] = PartActFormSet(self.request.POST)
        else:
            context['actividadespar'] = PartActFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        actividadespar = context['actividadespar']
        if actividadespar.is_valid():
            response = super().form_valid(form)
            actividadespar.instance = self.object
            actividadespar.save()
            return response
        else:           
            return super(ActividadCreate, self).form_valid(form)

    @method_decorator(permission_required('control.add_persona',reverse_lazy('control:actividades')))
    def dispatch(self, *args, **kwargs):
            return super(ActividadCreate, self).dispatch(*args, **kwargs)


class ActividadUpdate(UpdateView):
    model = Actividad
    # fields = '__all__'
    form_class = ActividadForm
    success_url = reverse_lazy('control:actividades')
    template_name_suffix = '_crear'

    def get_context_data(self, **kwargs):
        context = super(ActividadUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['actividadespar'] = PartActFormSet(self.request.POST, instance=self.object)
            context['actividadespar'].full_clean()
        else:
            context['actividadespar'] = PartActFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        actividadespar = context['actividadespar']
        if actividadespar.is_valid():
            response = super().form_valid(form)
            actividadespar.instance = self.object
            actividadespar.save()
            return response
        else:
            return super(ActividadCreate, self).form_valid(form)

    @method_decorator(permission_required('control.change_persona',reverse_lazy('control:actividades')))
    def dispatch(self, *args, **kwargs):
            return super(ActividadUpdate, self).dispatch(*args, **kwargs)

class ActividadDelete(DeleteView):
    model = Actividad
    success_url = reverse_lazy('control:actividades')
    template_name_suffix = '_eliminar'

    @method_decorator(permission_required('control.delete_persona',reverse_lazy('control:actividades')))
    def dispatch(self, *args, **kwargs):
            return super(ActividadDelete, self).dispatch(*args, **kwargs)