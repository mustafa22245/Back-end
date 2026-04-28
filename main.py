from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "أهلاً بك! سيرفر تطبيق الحلة الجامعي يعمل بنجاح."}

