# 🛒 Ecommerce API

Ecommerce API — bu Django asosida yaratilgan, onlayn do‘kon uchun backend REST API tizimi. Loyihada mahsulotlar bilan ishlash, toifadagi ma’lumotlarni olish, ma’lumotlarni yaratish, yangilash va o‘chirish imkoniyatlari mavjud.

---

## ⚙️ Texnologiyalar

- **Python 3**
- **Django**
- **Django REST Framework**
- **Docker & Docker Compose**
- **SQLite3** (test maqsadida)
- `.env` fayl orqali sozlamalarni ajratish

---

## 📁 Loyihaning tuzilmasi

Ecommerce_api/
- ├── config/ # Django konfiguratsiyasi (settings, urls)
- ├── products/ # Mahsulotlar uchun API (model, view, serializer)
- ├── requirements.txt # Kutubxonalar ro‘yxati
- ├── Dockerfile # Docker imiji uchun fayl
- ├── docker-compose.yml # Xizmatlarni boshqarish
- ├── .env # Muhit o‘zgaruvchilari
- └── db.sqlite3 # Mahalliy test bazasi


## 🐳 Docker orqali ishga tushurish

```
docker-compose up --build
```

## 📦 API funksiyalari
 Mahsulotlar ro‘yxati (GET)

 Mahsulot yaratish (POST)

 Mahsulotni yangilash (PUT/PATCH)

 Mahsulotni o‘chirish (DELETE)

 JWT orqali autentifikatsiya (agar mavjud bo‘lsa)
 
 Flash Sale - Aksiya yaratish, rejalashtirish

 Savat (Cart), Buyurtma (Order), To‘lov (Payment) [kelajakda]

## 🤝 Muallif
- 👤 Ism: Abdimajidov To‘lqinbek
- 📧 Email: tulqinjonabdimajidovhp@gmail.com
- 🌐 GitHub: AbdimajidovDev