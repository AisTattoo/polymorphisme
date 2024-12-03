class Rumah:
    def __init__(self, alamat="", atap=""):
        self.alamat = alamat
        self.atap = atap

    def deskripsi(self):
        print("Ini adalah sebuah rumah.")

    # Metode yang akan menunjukkan polymorphism
    def display(self):
        print(f"Alamat rumah ini adalah: {self.alamat}")

    def bentuk(self):
        print(f"Atap rumah ini adalah: {self.atap}")

    def fasilitas(self):
        print("Rumah ini memiliki fasilitas standar.")

class Apartemen(Rumah):
    def fasilitas(self):
        print("Apartemen ini memiliki kolam renang dan gym.")

class Villa(Rumah):
    def fasilitas(self):
        print("Villa ini memiliki taman pribadi dan area BBQ.")

# Fungsi polymorphism
def info_rumah(rumah):
    rumah.deskripsi()
    rumah.display()
    rumah.bentuk()
    rumah.fasilitas()
    print()  # Baris kosong untuk memisahkan output

# Membuat objek dengan tipe yang berbeda
apartemen_jakarta = Apartemen(alamat="Jl. Sudirman No. 10, Jakarta", atap="Coklat")
villa_bali = Villa(alamat="Jl. Diponegoro No. 15, Bali", atap="Hitam")

# Menggunakan fungsi yang sama untuk objek dengan tipe berbeda
info_rumah(apartemen_jakarta)  # Output akan sesuai implementasi kelas Apartemen
info_rumah(villa_bali)         # Output akan sesuai implementasi kelas Villa
