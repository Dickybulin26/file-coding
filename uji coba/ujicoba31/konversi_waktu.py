

# detik = input("masukan detik = ")

# hari = detik / 86400
# jam = (detik%86400)/3600
# menit = ((detik % 86400)/3600)/60
# # sisa_detik = (((detik%86400)%3600)%60)

# print(f"sisa_detik = {detik}")

def main():
    # menampilkan informasi program
    print("Konversi Detik ke Jam\n")

    # input total detik
    totaldetik = int(input("Masukkan detik \t: "))

    # melakukan konversi hh:mm:ss ke detik
    hh = totaldetik // 3600
    sisadetik = totaldetik % 3600
    mm = sisadetik // 60
    ss = sisadetik % 60

    # menampilkan hasil konversi
    print("%d detik sama dengan %d:%d:%d" %(totaldetik,hh,mm,ss))

if __name__ == "__main__":
    main()

