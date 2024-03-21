from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, HTTPException
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve i file statici dalla cartella build
app.mount("/static", StaticFiles(directory="./frontend/build/static"), name="static")

# Route per la home page
@app.get("/", response_class=JSONResponse)
async def serve():
    try:
        with open("frontend/build/index.html", "r") as file:
            return file.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route per gestire le richieste POST all'endpoint /api/sendText
app.post("/api/sendText")
async def hello(request: Request):
    data = await request.json()
    text = data.get('text')
    # Usiamo il modello per elaborare il testo
    return JSONResponse(content={"message": "YES"})  # Risposta dal modello

# Esegui l'applicazione FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
