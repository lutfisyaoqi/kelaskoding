from abc import ABC, abstractmethod

# Kelas abstrak
class Kendaraan(ABC):
    @abstractmethod
    def nyalakan(self):
        pass

# Class turunan Mobil
class Mobil(Kendaraan):
    def nyalakan(self):
        return "Mobil berhasil dinyalakan! Brumm..."

# Class turunan Motor
class Motor(Kendaraan):
    def nyalakan(self):
        return "Motor mogok! Tidak bisa dinyalakan."

# Contoh penggunaan
if __name__ == "__main__":
    mobil = Mobil()
    motor = Motor()

    print("Coba nyalakan mobil:")
    print(mobil.nyalakan())  # memanggil dan menampilkan hasil return

    print("\nCoba nyalakan motor:")
    print(motor.nyalakan())  # memanggil dan menampilkan hasil return
