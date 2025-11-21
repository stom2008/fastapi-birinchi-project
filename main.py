from fastapi import FastAPI

app = FastAPI()

mevalar = ["olma", "anor"]

@app.get("/")
def index():
    return {"mevalar_list": mevalar}



@app.post("/{meva_nomi}")
def meva_yaratish(meva_nomi):
    global mevalar
    mevalar.append(meva_nomi)
    return {"message": "meva yaratildi."}


@app.put("/{meva_nomi}/{yangi_nom}")
def ozgartirish(meva_nomi: str, yangi_nom: str):
    global mevalar 
    try:
        meva_id = mevalar.index(meva_nomi)
        mevalar[meva_id] = yangi_nom
    except:
        return {"error": "bunday meva nomi yo'q"}
    return {"xabar": "meva nomi o'zgardi"}

@app.put("/{meva_nomi}/{yangi_nom}")
def ozgartirish(meva_nomi: str):
    global mevalar 
    try:
        mevalar.remove(meva_nomi)
    except:
        return {"error": "bunday meva nomi yo'q"}
    return {"xabar": "meva nomi o'zgardi"}

