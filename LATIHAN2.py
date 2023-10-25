import re

# Data input
data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# Fungsi untuk mengambil hanya nilai integer dari string
def ambil_integer(d):
    return re.findall(r'\d+', d)

# Menggunakan fungsi filter dan ambil_integer untuk mengambil nilai integer
for waktu_str in data:
    nilai_integer = ambil_integer(waktu_str)
    print(nilai_integer)