# Tugas 2 — Authentication & Authorization

Project ini dibuat untuk tugas mata kuliah **Pengantar Keamanan Perangkat Lunak (Genap 2025/2026)**.
Fokus tugas ini adalah implementasi **authentication dan authorization** pada web Django.

## AnonymousPacil

| Nama                   | NPM        |
| ---------------------- | ---------- |
| Farras Syafiq U        | 2406495722 |
| Neal Guarddin          | 2406348282 |
| Muhammad Fazil Tirtana | 2306274983 |
| Izzudin Abdul Rasyid   | 2406495786 |
| Najwa Zarifa           | 2306207796 |

## Fitur

* **Biodata publik**
  Halaman utama menampilkan biodata anggota kelompok dan bisa dilihat tanpa login.

* **Login dengan Google OAuth**
  Login menggunakan akun Google dengan `django-allauth`.

* **Authorization anggota**

  * User yang email-nya ada di database biodata dianggap anggota.
  * Anggota bisa membuka halaman settings dan mengubah tampilan web (warna, font, dll).
  * User lain hanya bisa melihat halaman utama.

* **Dynamic site settings**
  Pengaturan tampilan disimpan di database dan langsung diterapkan ke halaman.

## Cara menjalankan

Install dependency:

```bash
pip install -r requirements.txt
```

Migrasi database:

```bash
python manage.py migrate
```

Seed data anggota (supaya email cocok dengan akun Google):

```bash
python seed.py
```

Jalankan server:

```bash
python manage.py runserver
```

Buka di browser:

```
http://127.0.0.1:8000/
```
