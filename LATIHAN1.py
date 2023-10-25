# Fungsi untuk mengkonversi waktu menjadi menit
def waktu_ke_menit(minggu):
    def hari(hari):
        def jam(jam):
            def menit(menit):
                total_menit = (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
                return total_menit
            return menit
        return jam
    return hari

# Data input
data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# Menggunakan fungsi currying untuk mengonversi data
for waktu_str in data:
    waktu_split = waktu_str.split()
    minggu = int(waktu_split[0])
    hari = int(waktu_split[2])
    jam = int(waktu_split[4])
    menit = int(waktu_split[6])

    total_menit = waktu_ke_menit(minggu)(hari)(jam)(menit)
    print(f"{waktu_str} = {total_menit} menit")