from django.urls import path

from . import views

app_name = 'control'
urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('personas/', views.PersonaListView.as_view(), name='personas'),
    path('persona/<int:pk>', views.PersonaDetailView.as_view(), name='persona-detail'),
    path('comunidades/', views.ComunidadListView.as_view(), name='comunidades'),
    path('comunidad/<int:pk>', views.ComunidadDetailView.as_view(), name='comunidad-detail'),
    path('actividades/', views.ActividadListView.as_view(), name='actividades'),
    path('actividad/<int:pk>', views.ActividadDetailView.as_view(), name='actividad-detail'),
]

# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('persona/create/', views.PersonaCreate.as_view(), name='persona_create'),
    path('persona/<int:pk>/update/', views.PersonaUpdate.as_view(), name='persona_update'),
    path('persona/<int:pk>/delete/', views.PersonaDelete.as_view(), name='persona_delete'),
]

urlpatterns += [
    path('comunidad/create/', views.ComunidadCreate.as_view(), name='comunidad_create'),
    path('comunidad/<int:pk>/update/', views.ComunidadUpdate.as_view(), name='comunidad_update'),
    path('comunidad/<int:pk>/delete/', views.ComunidadDelete.as_view(), name='comunidad_delete'),
]

urlpatterns += [
    path('actividad/create/', views.ActividadCreate.as_view(), name='actividad_create'),
    path('actividad/<int:pk>/update/', views.ActividadUpdate.as_view(), name='actividad_update'),
    path('actividad/<int:pk>/delete/', views.ActividadDelete.as_view(), name='actividad_delete'),
]
