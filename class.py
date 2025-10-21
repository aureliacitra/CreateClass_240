# membuat persegi panjang dan konstruktor 
class Persegipanjang:
 def __init__(self, panjang, lebar):
    self.panjang = panjang
    self.lebar = lebar

# menghitung keliling
def keliling(self):
    return 2 * (self.panjang * self.lebar)

# menghitung luas
def luas(self):
    return self.panjang * self.lebar

# fungsi __str__ untuk menmpilkan string objek
def __str__(self):
    return f"Persegi panjang, panjang (self.panjang) cm, dan lebar (self.lebar) cm"

try: 
  panjang_input = int(input("masukkan panjang (cm):"))
  lebar_input = int(input("masukkan lebar (cm): "))

# membuat objek dari kelas persegi panjang
  pp = Persegipanjang(panjang_input, lebar_input)
  print("Keliling:", pp.keliling(), "cm")
  print("Luas", pp.Luas(), "cm^2")

except ValueERrror:
    print("Input harus berupa angka.")
