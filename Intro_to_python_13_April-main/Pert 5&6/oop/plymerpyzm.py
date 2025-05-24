from abc import ABC, abstractmethod

# Kelas abstrak
class Kendaraan(ABC):
    @abstractmethod
    def nyalakan(self):
        pass

# Class Mobil mewarisi Kendaraan
class Mobil(Kendaraan):
    def nyalakan(self):
        return "Mobil menyala dengan suara Brumm..."

# Class Motor mewarisi Kendaraan
class Motor(Kendaraan):
    def nyalakan(self):
        return "Motor menyala tapi kemudian mogok..."

# Fungsi yang menerapkan polimorfisme
def coba_nyalakan(kendaraan: Kendaraan):
    print(kendaraan.nyalakan())

# Contoh penggunaan
if __name__ == "__main__":
    daftar_kendaraan = [Mobil(), Motor()]

    for k in daftar_kendaraan:
        coba_nyalakan(k)
