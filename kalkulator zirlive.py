class kalkulator:
    def tambah(self,a,b):
        hasil = a+b
        print (f"hasil dari {a}{o}{b} adalah {hasil}")
    def kurang(self,a,b):
        hasil = a-b
        print (f"hasil dari {a}{o}{b} adalah {hasil}")
    def kali(self,a,b):
        hasil = a*b
        print (f"hasil dari {a}{o}{b} adalah {hasil}")
    def bagi(self,a,b):
        if b == 0:
            print("tidak dapat dibagi 0")
        else:
            hasil = a/b
            print(f"hasil dari {a}{o}{b} adalah {hasil} ")
        
cal = kalkulator ()
while True:
    print(" aplikasi kalkulator sederhana ")
    print("=============================")
    print("1. kalkulator")
    print("2. keluar")
    s1 = int(input("masukkan pilihan 1/2: "))
    if s1 ==1:
        a = int(input("masukkan angka pertama: "))
        b = int(input("masukkan angka kedua: "))
        print("metode oprasi: ")
        print("1. penjumlahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        o = str(input("masukkan operasi: "))
        if o=='+':
            cal.tambah(a,b)
        elif o =='-':
            cal.kurang (a,b)
        elif o =='/':
            cal.bagi (a,b)
        elif s1 == 2:
            print("terima kasih")
            
    
