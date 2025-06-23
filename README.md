# Stima_Makalah_13523081


## Deskripsi

Program ini menyelesaikan puzzle lantai es di Sootopolis City Gym pada game Pokémon Emerald, dengan aturan pemain harus menginjak semua ubin yang dapat diinjak sekali saja dan mengakhiri langkah di ubin terakhir yang berada tepat sebelum tangga ke stage berikutnya (G). Tantangan utama dari puzzle ini adalah menemukan jalur yang melewati semua ubin sekali saja tanpa terjebak, karena kesalahan langkah kecil bisa membuat solusi menjadi tidak mungkin.

Program ini menggunakan algoritma backtracking untuk menjelajahi semua kemungkinan jalur dari titik awal ke titik tujuan. Setiap langkah direkam, dan jika menemui jalan buntu atau tidak mungkin mencapai semua ubin tersisa, program akan kembali (backtrack) ke langkah sebelumnya.

## Cara Menjalankan

1. Clone repository ini:

```bash
git clone https://github.com/JethroJNS/Stima_Makalah_13523081.git
```

2. Navigasi ke direktori repositori dan jalankan command berikut:

```bash
cd src
```

```bash
python sootopolis_gym_puzzle_solver.py
```