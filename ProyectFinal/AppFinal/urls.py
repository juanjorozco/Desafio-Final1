from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('personalApi/', views.personalApi),
    path('estudiosApi/', views.estudiosApi),
    path('experienciaApi/', views.experienciaApi),
    path('personal/', views.personal,name="Personal"),
    path('estudios/', views.estudios,name="Estudios"),
    path('experiencia/', views.experiencia,name="Experiencia"),
    path('informacion/', views.informacion,name="Informacion"),
    path('busquedaEdad/', views.busquedaEdad),
    path('edad/',views.edad),
    path('busquedaAños/', views.busquedaAños),
    path('años/',views.años),
]