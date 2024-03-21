from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve i file statici dalla cartella build
app.mount("/static", StaticFiles(directory="/content/InformaticaUmanistica/frontend/build/static"), name="static")

# Route per la home page
@app.get("/", response_class=HTMLResponse)
async def serve():
    with open("frontend/build/index.html", "r") as file:
        return file.read()

# Route per gestire le richieste POST all'endpoint /api/sendText
@app.post("/api/sendText")
async def hello(request: Request):
    data = await request.json()
    text = data.get('text')
    # Usiamo il modello per elaborare il testo
    return JSONResponse(content={"message": "YES"})  # Risposta dal modello

# Esegui l'applicazione FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8084)
