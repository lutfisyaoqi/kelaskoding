# Case: Mengamati hewan

class Hewan:  # Nama class sebaiknya pakai huruf kapital (sesuai konvensi Python)
    _umur_hewan = 10  # Properti "protected" (konvensi)

    def __init__(self, nama_hewan):
        self.nama_hewan = nama_hewan  # Properti public

    def makan(self):
        print("Hewan sedang makan !!!!")

# Membuat objek
kucing = Hewan("Jamall")
print(f"Nama kucing: {kucing.nama_hewan}")

# _umur_hewan bisa diakses, tapi secara konvensi sebaiknya tidak langsung
# print(f"Umur hewan: {kucing._umur_hewan}")  # Aktifkan jika ingin lihat umur

print("Kucing sedang apa?")
kucing.makan()
