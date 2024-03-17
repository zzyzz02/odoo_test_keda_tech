# Hasil Test Odoo - Keda-Tech.com

Repositori ini berisi implementasi dari test yang diberikan oleh Keda-Tech.com, menunjukkan fungsi backend menggunakan Odoo. Test ini mencakup pembuatan sistem yang memungkinkan klien untuk mengelola material, termasuk melihat semua material, memfilter berdasarkan jenis material, memperbarui, dan menghapus material.

## Overview

Kebutuhan untuk test ini termasuk:

- **Melihat Material**: Klien harus dapat melihat semua material yang telah dibuat dan memfilternya berdasarkan jenis material.
- **Memperbarui Material**: Klien harus dapat memperbarui informasi tentang satu material.
- **Menghapus Material**: Klien harus dapat menghapus satu material.

Berikut hasil pengembangan yang sudah saya lakukan berdasarkan requirement awal:

1. Membuat ERD (Diagram Hubungan Entitas) untuk kebutuhan klien.
2. Mengembangkan Model.
3. Mengimplementasikan Controller untuk membuat REST API yang memenuhi persyaratan di atas.
4. Menulis Unit testing untuk fungsi yang diimplementasikan.

## Kebutuhan Tambahan

Setiap material harus memiliki informasi berikut:

1. Kode Material
2. Nama Material
3. Tipe Material (dropdown dengan 3 pilihan: Fabric, Jeans, Cotton)
4. Harga Beli Material
5. Supplier Terkait (dropdown: nama supplier)

Seluruh informasi tersebut harus terisi, dan untuk harga beli material tidak boleh nilai < 100.

## ERD (Diagram Hubungan Entitas)

ERD untuk proyek ini menggambarkan struktur database dan hubungan antar entitas, yang dapat dilihat pada file "Erd Material Registration.png"


## Controller

Controller dikembangkan untuk mengelola operasi API untuk material. Endpoint berikut diimplementasikan:

- `GET /api/material` - Mengambil semua material atau daftar terfilter berdasarkan jenis material.
- 'POST /api/material` - Menambahkan material kedalam daftar
- `PUT /material/:id` - Memperbarui detail material tertentu yang diidentifikasi oleh ID-nya.
- `DELETE /material/:id` - Menghapus material tertentu berdasarkan ID-nya.

  Untuk Lebih detail, bisa melihat dokumentasi yang ada pada link berikut https://documenter.getpostman.com/view/23857156/2sA2xnxVWn

## Unit Testing

Unit testing ditulis untuk memastikan keandalan dan fungsionalitas dari fitur yang dikembangkan. 
