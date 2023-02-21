class User:
    def __init__(self, nombre, apellido, telefono, cedula, email, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.cedula = cedula
        self.email = email
        self.contrasena = contrasena

    def toDBCollection(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'cedula': self.cedula,
            'email': self.email,
            'contrasena': self.contrasena
        }
