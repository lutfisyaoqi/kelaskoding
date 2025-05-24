class ibu:
    panggilan = "ini punya ibu"
    
    def memanggil(self):
        print("iya, anj")
        
    def setsifat(self,sifat):
        self.__sifat = sifat
        
    def getsifat(self):
        print("heh kamu anaakk haramm")
        
class anak(ibu):
    def suruh(self):
        print("nanti dulu anjay!!!!!")
        
toni = anak()
toni.panggilan = "toni"
print(f"siapa nama lu : {toni.panggilan}")
toni.memanggil()
toni.suruh()
toni.getsifat()