# Tugas Soal 24 – Interpolasi Newton Ordo 3

**Kelompok:** R05  
**Anggota:**    
- Fadhilla Dafa Karunia (5053241003)  
- Muhammad Yusuf Qardhawi (5053241026)
- Muhammad Zaki Alfikri (5053241034)
- Ahmad Habibie Dewa Pratama (5053241019)
- Fauzan Farhan Al Qodri Irawan (5053241018)

---

## Deskripsi Tugas
Tugas ini mengerjakan soal nomor 24 pada file **Tugas Program Komnum 2025.pdf**, yaitu melakukan interpolasi Newton ordo 3 untuk memperkirakan nilai fungsi pada titik \( x = 11 \) berdasarkan data:
- x₀ = 6 → f(x₀) = 234
- x₁ = 9 → f(x₁) = 960
- x₂ = 12 → f(x₂) = 2280
- x₃ = 15 → f(x₃) = 4356

## Penjelasan Kode
1. Semua nilai X yang diinisialisasi dalam array : 6, 9, 12, 15
2. Semua nilai f(x) yang diinisialisasi dalam array : 234, 960, 2280, 4356
3. Loop untuk menghitung nilai beda terbagi dengan rumus \( Beda Terbagi = (f[x_{i+j}] - f[x_i]) / (x_{i+j} - x_i) \)
4. Fungsi 'newton_interpolation' menerima nilai x_eval dan mengembalikan nilai interpolasi pada titik tersebut
5. Loop menghitung nilai interpolasi dengan rumus \( P(x) = f[x₀] + ∑ (f[x₀, x₁, ..., xₖ] * ∏ (x - xₖ)) \)
4. Hitung nilai interpolasi pada x = 11 dengan menggunakan fungsi 'newton_interpolation'
5. Print hasil dari interpolasi dengan pembulatan dua angka dibelakang koma

Hasil akhirnya adalah nilai taksir \( f(11) \) yang dibulatkan dua angka di belakang koma yakni f(11) = 1764.0