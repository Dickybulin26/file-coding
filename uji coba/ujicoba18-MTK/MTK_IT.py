# program matematika python

print("UJIAN MATEMATIKA DENGAN BAHASA PYTHON")


nama = input("masukan nama anda = ")
kelas = int(input('masukan kelas anda = '))
# soal

# 1.sebuah persegi panjang memiliki panjang 20cm dan lebar 10cm,hitunglah luasnya!

print("jawaban no 1")

panjang = 20
lebar = 10

luas = panjang * lebar
print("20 * 10 = ",luas)

# 2.UBAHLAH BILANGAN DESIMAL 625 MENJADI BILANGAN BINARY 

print("jawaban no 2")

desimal = int(625)
hasil = ""
while (desimal != 0) :
    hasil += ("%d" % (desimal % 2))
    desimal //= 2

hasilakhir = ""

for i in range(len(hasil)-1,-1,-1) :
    hasilakhir += hasil[i]
print("625 Binernya Adalah = ",hasilakhir)

# 3.UBAHLAH BILANGAN DESIMAL 246 KE BILANGAN OKTAL LALU DI MODULUS 2!
print("jawaban no 3")

desimal = int(264)

oktal = oct(desimal).replace("0o","264 oktalnya adalah = ")

print(oktal)

# 4.SEBUAH PERSEGI MEMILIKI PANJANG SISI 1050m HITUNGLAH LUASNYA LALU HASILNYA DIMODULUSKAN 2 DAN UBAH KE BILANGAN HEXADESIMAL!

print("jawaban no 4")

panjang_sisi = 1050

luas = panjang_sisi ** 2
modulus = luas // 2

'''desimal => biner'''

desimal = int(modulus)
hexa = hex(desimal).replace("0x","1050**2 // 2 = 1102500//2 = 551250 => hexadesimal = ")

print(hexa)

# 5.SELESAIKAN SOAL BERIKUT! 
    # A.(1000**2) + 625 / 144 - 246 % 2 // 3 * 50
    # B.LALU HASILNYA DIKONVERSIKAN MENJADI BILANGAN HEXADESIMAL,BINER,DAN OKTAL

print("jawaban no 5")
print('jawaban A')

A = (1000**2) + 625 / 144 - 246 % 2 // 3 * 50
print("(1000**2) + 625 / 144 - 246 % 2 // 3 * 50 = ",A)

print('jawaban B')

hasil_A = int(A)

biner = bin(hasil_A).replace("0b",'binernya adalah = ')
oktal = oct(hasil_A).replace("0o",'oktalnya adalah = ')
hexa = hex(hasil_A).replace("0x",'hexanya adalah = ')

print(biner)
print(oktal)
print(hexa)

# 6.BUAT LAH PROGRAM KONVERSI SUHU CELCIUS KE KELVIN,FAHRENHEIT,DAN REAMUR!
print("jawaban no 6")

print('konversi suhu celcius ke kelvin,fahrenheit,dan reamur')

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(150)
print("suhu adalah ",celcius, 'celcius')

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, 'reamur')

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, 'fahrenheit')

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, 'kelvin')

# 7.BUATLAH PROGRAM KONVERSI SUHU SATUAN DIBAWAH INI!
# A.FAHRENHEIT => KELVIN
# B.KELVIN => FAHRENHEIT

print("jawaban no 7")

suhu = 90.5

print("jawaban A")

print('suhu fahrenheit = ',suhu)

fahrenheit = float(suhu)
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin: ", kelvin)

print('jawaban B')

print('suhu kelvin = ',suhu)

kelvin = float(suhu)
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit: ", fahrenheit)

# 8.BUATLAH PROGRAM LOOPING / PENGULANGAN MENGGUNAKAN WHILE LOOP UNTUK KATA "Hello World!" SEBANYAK 10x!
print('jawaban no 8')

print("while loop")

count = 0
while (count < 9):
    print('Hello World!',count)
    count = count + 1
print("Hello World!")

# 9.BUAT LAH PROGRAM LOOPING / PENGULANGAN MENGGUNAKAN FOR LOOP UNTUK KATA "Hello World!" 
print("jawaban no 9")

print('for loop')

kata = "Hello World!"
for x in kata:
    print (x)

# 10.BUAT LAH PROGRAM LOOPING / PENGULANGAN MENGGUNAKAN NESTED LOOP UNTUK KATA "Hello World!" 
print("jawaban no 10")

print("nested loop")

i = 0
while(i < 10):
    j = 4
    while(j <= (i/j)):
        if not(i%j): break
        j =  j + 1
    if (j > i/j) : print(i,"Hello World!")
    i = i + 1



