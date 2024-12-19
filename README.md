# Nama Proyek: Car Dealer Website

## Deskripsi Proyek
Website ini dirancang untuk memberikan layanan lengkap bagi dealer mobil, termasuk manajemen daftar mobil, pemesanan test drive, dan pengelolaan data pelanggan. Dibangun dengan **Django**, website ini mendukung user role-based access control untuk admin, staf, dan pelanggan.

---

## Fitur Utama
### 1. Untuk Admin dan Staf
- **Manajemen Mobil**: Tambah, edit, dan hapus mobil yang tersedia.
- **Manajemen Pemesanan Test Drive**: Melihat daftar pemesanan test drive.
- **Notifikasi**: Menampilkan popup setelah melakukan tindakan sukses.

### 2. Untuk Pelanggan
- **Pemesanan Test Drive**: Pelanggan dapat memilih mobil dan memesan slot test drive.
- **Riwayat Pemesanan**: Melihat status pemesanan mereka.
- **Deskripsi Detail Mobil**: Informasi lengkap setiap mobil.

---

## Teknologi yang Digunakan
- **Backend**: Django Framework (Python)
- **Frontend**: Bootstrap 5, HTML, CSS, dan JavaScript
- **Database**: SQLite (dapat ditingkatkan ke PostgreSQL atau MySQL)
- **Library Pendukung**: 
  - FontAwesome untuk ikon
  - Django Signals untuk penghapusan file otomatis
  - Validasi berbasis custom pada model

---

## Panduan Instalasi
### Prasyarat
- Python 3.8 atau lebih baru
- Virtualenv
- Git

### Langkah-Langkah
1. Clone repositori:
   ```bash
   git clone https://github.com/username/car-dealer.git
   cd car-dealer
2. Buat virtual environment dan aktifkan
   ```bash   
   python -m venv env
   source env/bin/activate # (Linux/MacOS)
   env\Scripts\activate # (Windows)
3. Instal dependensi:
   ```bash   
   pip install -r requirements.txt
4. Migrasikan database:
   ```bash   
   python manage.py migrate
5. Jalankan server lokal:
   ```bash   
   python manage.py runserver
6. Buka di browser: http://127.0.0.1:8000

## Dokumentasi API

### 1. Endpoint Utama

#### a. Mobil
- **GET /cars/**  
  Mendapatkan daftar semua mobil.

- **POST /cars/add/**  
  Menambahkan mobil baru. *(Hanya untuk admin/staf)*

---

#### b. Test Drive
- **POST /test-drive/**  
  Membuat pemesanan test drive.

- **GET /test-drive/list/**  
  Melihat daftar pemesanan. *(Hanya untuk admin/staf)*
