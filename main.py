from fastapi import FastAPI
from backend.adapters.controllers import usuario_controller

app = FastAPI()

# incluimos el router
app.include_router(usuario_controller.router)

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}
