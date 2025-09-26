from fastapi import FastAPI
from adapters.controllers import usuario_controller

app = FastAPI(title="Gestión de Empleados")

# incluir las rutas
app.include_router(usuario_controller.router)

@app.get("/")
def root():
    return {"message": "API de Gestión de Empleados funcionando 🚀"}
