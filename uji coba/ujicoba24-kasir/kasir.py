# # nama toko dan menu toko
# print('toko siudin')
# print('tersedia menu: ')
# print('1. Es teh     -> Rp.3000')
# print('2. bubur ayam -> Rp.5000')
# print('Beli 2 bubur Dapat Diskon 20%')

# # pembelian
# opsi = input("Pilih menunya no : ")
# jumlah = int(input('jumlah : '))
# uang_kamu = int(input("uang kamu : "))
# harga = 3000
# diskon = 20/100
# kembalian = uang_kamu - harga
# # cetak pembelian
# print(f"Kamu membeli Es teh berjumlah : {jumlah}")
# print(f'dengan harga : {harga}')
# print(f'sisa uang kembalian : {kembalian}')

# # opsi diskon
# if opsi == '1':
#     jumlah = int(input('jumlah : '))
#     uang_kamu = int(input("uang kamu : "))
#     harga = 3000
#     diskon = 20/100
#     kembalian = uang_kamu - harga

# # pembelian dengan jumlah 1
# if jumlah == 1:
#         print(f"Kamu membeli Es teh berjumlah : {jumlah}")
#         print(f'dengan harga : {harga}')
#         print(f'sisa uang kembalian : {kembalian}')

# # pembelian dengan jumlah 2
# elif jumlah == 2:
#     print("kamu membeli es teh berjumlah : ",jumlah,'dan mendapatkan diskon sebesar 20%')
#     print('dengan harga : ',harga)
#     print("total diskon : ",harga*jumlah*20/100)


# toko 2
print('tokonya si asep')
print('MENU TOKO:')
print('1. Susu      : Rp.3000')
print('2. Es teh    : Rp.2000')
print('3. Kopi susu : Rp.4000')
print("Akan mendapatkan diskon jika membeli 2 item sekaligus sebesar 20%")

susu = '1'
es_teh = '2'
kopi_susu = '3'

beli = input("pilih menu no : ")
jumlah = int(input("beli sebanyak : "))
uang = int(input("berapa banyak uang kamu : "))

if beli == susu:
    harga = 3000
    diskon = 20/100
    pembelian = jumlah * harga
    kembalian = pembelian - uang
    if pembelian > uang:
        kembalian = uang - pembelian
        print(f'\nharga total : {pembelian}')
        print(f'sisa uang kamu : {kembalian}')
    elif jumlah == 2:
        print(f"kamu membeli sebanyak : {jumlah}",'dan mendapatkan diskon 20%')
        print(f'dengan harga : {harga}')
        print(f'total diskon : {harga*jumlah*diskon}')
    else:
        print(f'\nharga total : {pembelian}')
        print(f'sisa uang kamu : {kembalian}')