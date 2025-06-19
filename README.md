# 📚 Automated API Testing & Load Testing - Django Ninja x Locust

## Fitur Utama

- Backend dikembangkan dengan **Django Ninja**
- Model:
  - `Course`: menyimpan data kursus
  - `CourseMember`: relasi banyak ke banyak dengan `User` dan peran (Teacher/Student)
- Endpoint utama:
  - `GET /api/courses`: Menampilkan daftar kursus (hanya untuk user login)
  - `POST /api/courses`: Menambahkan kursus baru (diperlukan login)
- Autentikasi menggunakan user:
  - **Username:** `teacher1`
  - **Password:** `pass123`
- Load testing dilakukan menggunakan **Locust** pada endpoint `GET` dan `POST`

---

## Cara Menjalankan

### 1. Jalankan Server Django

```bash
python manage.py runserver
locust --host=http://127.0.0.1:8000
```
