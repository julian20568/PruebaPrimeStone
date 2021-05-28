1. Se crearon tres modelos conforme al diseño de la bd, se implemento componentes de serializadores que nos 
ofrece django restframework lo cual nos permite que las estructuras complejas y los modelos de nuestro 
proyecto en django se conviertan a estructuras nativas de python y se conviertan facilmente a formato JSON 
o XML

2. Se creo una vista diferente para cada clase del modelo donde se realiza el crud completo de cada modelo.

3. Se creo un archivo de rutas dentro de la app CrudEstudiantes donde se crean todas las urls para realizar las diferentes 
consultas de los metodos creados en las vistas.

4. Para realizar consultas tanto de estudiantes, cursos, y direcciones se crearon diferentes parametros por los cuales podemos hacerlo, ejemplo por id, nombre etc.

Datos de prueba

User: prueba <-->
Pass: 123 <-->
Tocken: 643dd9a829640eaf49892e5016a37db9e3e8d639

Agregar Cursos
{ 
  "nombre": "Python",
  "duracion": "6 meses",
  "costo": 500000,
  "fecha_inicio": "2021-05-31",
  "fecha_fin": "2021-11-01"
}

Agregar direcciones
{ 
  "pais": "Colombia",
  "ciudad": "Popayán",
  "barrio": "Yanaconas",
  "direccion": "cra 3 28N-60"
}


Agregar Estudiantes
{ 
  "nombre": "Juan",
  "apellido": "Escobar",
  "num_documento": 1003798090,
  "num_telefono": 3218532010,
  "correo": "juan21@hotmail.com",
  "genero": "Masculino",
  "fecha_nacimiento": "1995-02-20",
  "cod_curso": 5,
  "cod_direcciones": 2
}
