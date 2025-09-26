class Usuario:
    def __init__(self, id: int, nombre: str, email: str, rol: str):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __repr__(self):
        return f"<Usuario {self.id} - {self.nombre} ({self.rol})>"
