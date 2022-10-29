print("program diskon")
print("Diskon total sampai 35 persen setiap pembelian lebih dari Rp100.000")

# total_harga = int(input("Total Harga = "))

# if total_harga < 100000:
#     diskon = total_harga * (35/100)

# else:
#     print(f"Total harga yangn anda bayar adalah = {total_harga}")

total = int(input("Total harga = "))
setelah_diskon = total

if total < 100000:
    diskon = total * (5/100)
else:
    diskon = total * (10/100)

setelah_diskon = total - diskon
print('diskonya yaitu : {}'.format(int(diskon)))
print('Harga setelah diskon : {}'.format(int(setelah_diskon)))