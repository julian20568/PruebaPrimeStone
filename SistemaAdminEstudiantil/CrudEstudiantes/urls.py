from django.urls import path
from CrudEstudiantes import views_cursos
from CrudEstudiantes import views_direcciones
from CrudEstudiantes import views_estudiantes

urlpatterns=[
    ############################
    #RUTAS PARA LA CLASE CURSOS#
    ############################
    path('cursos',views_cursos.MetCursos),
    path('cursos/<int:key>',views_cursos.cursos_detail),
    path('cursos/nombre/<str:nom>', views_cursos.Curso_nombre),
    path('cursos/duracion/<str:dur>', views_cursos.Curso_duracion),
    path('cursos/costo/<int:cost>', views_cursos.Curso_costo),

    #################################
    #RUTAS PARA LA CLASE DIRECCIONES#
    #################################
    path('direcciones',views_direcciones.MetDirecciones),
    path('direcciones/<int:key>',views_direcciones.direcciones_detail),
    path('direcciones/pais/<str:ps>',views_direcciones.Dir_pais),
    path('direcciones/ciudad/<str:ciu>',views_direcciones.Dir_ciudad),
    path('direcciones/barrio/<str:bar>',views_direcciones.Dir_barrio),
]

