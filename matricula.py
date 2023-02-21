class Matricula:
    def __init__(self,promedio_estudiante, nombre_estudiante, apellido_estudiante, lugar_nacimiento_estudiante, fecha_nacimiento_estudiante, cedula_estudiante, curso_estudiante, contacto_estudiante, email_estudiante, nombre_representante, apellido_representante, edad_representante, cedula_representante, profesion_representante, contacto_representante, correo_representante, lugar_trabajo_representante, nombre_madre,apellido_madre,edad_madre,instruccion_madre,profesion_madre,contacto_madre,lugar_trabajo_madre,nombre_padre,apellido_padre,instrucion_padre,profesion_padre,contacto_padre,lugar_trabajo_padre,edad_padre):
        self.nombre_estudiante = nombre_estudiante
        self.apellido_estudiante = apellido_estudiante
        self.lugar_nacimiento_estudiante = lugar_nacimiento_estudiante
        self.fecha_nacimiento_estudiante = fecha_nacimiento_estudiante
        self.cedula_estudiante = cedula_estudiante
        self.curso_estudiante = curso_estudiante
        self.contacto_estudiante = contacto_estudiante
        self.email_estudiante = email_estudiante
        self.promedio_estudiante = promedio_estudiante
        self.matriculado = False,

        self.nombre_representante = nombre_representante
        self.apellido_representante = apellido_representante
        self.edad_representante = edad_representante
        self.cedula_representante = cedula_representante
        self.profesion_representante = profesion_representante
        self.contacto_representante = contacto_representante
        self.correo_representante = correo_representante
        self.lugar_trabajo_representante = lugar_trabajo_representante

        self.nombre_madre = nombre_madre
        self.apellido_madre = apellido_madre
        self.edad_madre = edad_madre
        self.instruccion_madre = instruccion_madre
        self.profesion_madre = profesion_madre
        self.contacto_madre = contacto_madre
        self.lugar_trabajo_madre = lugar_trabajo_madre

        self.nombre_padre = nombre_padre
        self.apellido_padre = apellido_padre
        self.edad_padre = edad_padre
        self.instrucion_padre = instrucion_padre
        self.profesion_padre = profesion_padre
        self.lugar_trabajo_padre = lugar_trabajo_padre
        self.contacto_padre = contacto_padre

    def toDBCollection(self):
        return {
            'nombre_estudiante': self.nombre_estudiante,
            'apellido_estudiante': self.apellido_estudiante,
            'lugar_nacimiento_estudiante': self.lugar_nacimiento_estudiante,
            'fecha_nacimiento_estudiante': self.fecha_nacimiento_estudiante,
            'cedula_estudiante': self.cedula_estudiante,
            'curso_estudiante': self.curso_estudiante,
            'contacto_estudiante': self.contacto_estudiante,
            'email_estudiante': self.email_estudiante,
            'promedio_estudiante': self.promedio_estudiante,
            'matriculado': self.matriculado,

            'nombre_representante': self.nombre_representante,
            'apellido_representante': self.apellido_representante,
            'edad_representante': self.edad_representante,
            'cedula_representante': self.cedula_representante,
            'profesion_representante': self. profesion_representante,
            'contacto_representante': self.contacto_representante,
            'correo_representante': self.correo_representante,
            'lugar_trabajo_representante': self.lugar_trabajo_representante,

            'nombre_madre': self.nombre_madre,
            'apellido_madre': self.apellido_madre,
            'edad_madre': self.edad_madre,
            'instruccion_madre': self.instruccion_madre,
            'profesion_madre': self.profesion_madre,
            'contacto_madre': self.contacto_madre,
            'lugar_trabajo_madre': self.lugar_trabajo_madre,

            'nombre_padre': self.nombre_padre,
            'apellido_padre': self.apellido_padre,
            'edad_padre': self.edad_padre,
            'instruccion_padre': self.instrucion_padre,
            'profesion_padre': self.profesion_padre,
            'contacto_padre': self.contacto_padre,
            'lugar_trabajo_padre': self.lugar_trabajo_padre
        }
