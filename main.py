from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="تطبيق الحلة الجامعي")

# إعداد CORS للسماح لتطبيقك بالاتصال
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# قاعدة بيانات وهمية (مؤقتة في الذاكرة لتشغيل التطبيق)
# ---------------------------------------------------------
db = {
    "categories": {
        "قسم عام": {
            "ملزمة تجريبية": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        }
    },
    "tips": [
        "مرحباً بك في تطبيق الحلة الجامعي الإصدار الجديد!",
        "نظم وقتك بين الدراسة والراحة لتصل إلى التفوق."
    ]
}

# ---------------------------------------------------------
# الروابط (Endpoints) التي يطلبها تطبيق الهاتف
# ---------------------------------------------------------

@app.get("/")
def read_root():
    return {"message": "سيرفر Vercel يعمل بنجاح"}

@app.get("/get_tip")
def get_tip():
    if db["tips"]:
        return {"tip": random.choice(db["tips"])}
    return {"tip": "لا توجد نصائح حالياً. استخدم لوحة التحكم لإضافة نصيحة!"}

@app.get("/get_categories")
def get_categories():
    return list(db["categories"].keys())

@app.get("/get_files/{category}")
def get_files(category: str):
    # إرجاع ملفات القسم المطلوب، وإذا لم يوجد نرجع قائمة فارغة
    return db["categories"].get(category, {})

@app.get("/get_db")
def get_db():
    return db

@app.post("/save_db")
def save_db(new_db: dict = Body(...)):
    global db
    db.update(new_db)
    return {"status": "success", "message": "تم الحفظ بنجاح"}

